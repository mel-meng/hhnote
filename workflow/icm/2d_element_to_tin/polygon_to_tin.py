"""
2D Zone Polygon to TIN Mesh Script for QGIS

This script converts 2D zone polygons (with depth/elevation attributes) into a TIN mesh
by interpolating values from polygon centroids to vertices.

Usage:
    Run this script in the QGIS Python Console or as a Processing script.
    
Author: Generated for ICM 2D Zone workflow
"""

from qgis.core import (
    QgsProject,
    QgsProcessingFeedback,
    QgsVectorLayer,
    QgsField,
    QgsExpression,
    QgsExpressionContext,
    QgsExpressionContextUtils,
    QgsFeature,
    QgsGeometry,
    QgsPointXY,
    QgsMeshLayer,
    QgsRasterLayer,
)
from qgis.PyQt.QtCore import QVariant, Qt
from qgis.PyQt.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QComboBox,
    QDoubleSpinBox,
    QPushButton,
    QMessageBox,
    QGroupBox,
    QCheckBox,
    QLineEdit,
    QFileDialog,
)
import processing


class PolygonToTinDialog(QDialog):
    """Dialog for selecting input parameters for the Polygon to TIN conversion."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("2D Zone to TIN Mesh")
        self.setMinimumWidth(400)
        self.setup_ui()
        self.populate_layers()
        
    def setup_ui(self):
        """Set up the dialog UI components."""
        layout = QVBoxLayout(self)
        
        # Layer selection group
        layer_group = QGroupBox("Input Layer")
        layer_layout = QVBoxLayout(layer_group)
        
        # 2D Zone Layer dropdown
        layer_row = QHBoxLayout()
        layer_row.addWidget(QLabel("2D Zone Layer:"))
        self.layer_combo = QComboBox()
        self.layer_combo.currentIndexChanged.connect(self.on_layer_changed)
        layer_row.addWidget(self.layer_combo)
        layer_layout.addLayout(layer_row)
        
        layout.addWidget(layer_group)
        
        # Field selection group
        field_group = QGroupBox("Field Selection")
        field_layout = QVBoxLayout(field_group)
        
        # Depth field dropdown (required)
        depth_row = QHBoxLayout()
        depth_row.addWidget(QLabel("Depth Field:"))
        self.depth_field_combo = QComboBox()
        depth_row.addWidget(self.depth_field_combo)
        field_layout.addLayout(depth_row)
        
        # Ground level field (required for water surface calculation)
        ground_row = QHBoxLayout()
        ground_row.addWidget(QLabel("Ground Level Field:"))
        self.ground_field_combo = QComboBox()
        ground_row.addWidget(self.ground_field_combo)
        field_layout.addLayout(ground_row)
        
        layout.addWidget(field_group)
        
        # Optional additional TIN group
        additional_group = QGroupBox("Additional TIN (Optional)")
        additional_layout = QVBoxLayout(additional_group)
        
        self.use_additional_field = QCheckBox("Create additional TIN")
        self.use_additional_field.stateChanged.connect(self.on_additional_field_toggled)
        additional_layout.addWidget(self.use_additional_field)
        
        additional_row = QHBoxLayout()
        additional_row.addWidget(QLabel("Additional Field:"))
        self.additional_field_combo = QComboBox()
        self.additional_field_combo.setEnabled(False)
        additional_row.addWidget(self.additional_field_combo)
        additional_layout.addLayout(additional_row)
        
        layout.addWidget(additional_group)
        
        # Processing options group
        options_group = QGroupBox("Processing Options")
        options_layout = QVBoxLayout(options_group)
        
        # Raster resolution
        resolution_row = QHBoxLayout()
        resolution_row.addWidget(QLabel("Raster Resolution:"))
        self.resolution_spin = QDoubleSpinBox()
        self.resolution_spin.setRange(0.01, 1000.0)
        self.resolution_spin.setValue(1.0)
        self.resolution_spin.setDecimals(2)
        self.resolution_spin.setSuffix(" units")
        resolution_row.addWidget(self.resolution_spin)
        options_layout.addLayout(resolution_row)
        
        layout.addWidget(options_group)
        
        # Output folder group
        output_group = QGroupBox("Output Location")
        output_layout = QVBoxLayout(output_group)
        
        folder_row = QHBoxLayout()
        folder_row.addWidget(QLabel("Output Folder:"))
        self.output_folder_edit = QLineEdit()
        self.output_folder_edit.setPlaceholderText("Select folder to save TIN files...")
        folder_row.addWidget(self.output_folder_edit)
        self.browse_button = QPushButton("Browse...")
        self.browse_button.clicked.connect(self.browse_output_folder)
        folder_row.addWidget(self.browse_button)
        output_layout.addLayout(folder_row)
        
        layout.addWidget(output_group)
        
        # Buttons
        button_layout = QHBoxLayout()
        self.run_button = QPushButton("Run")
        self.run_button.clicked.connect(self.accept)
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(self.run_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)
        
    def populate_layers(self):
        """Populate the layer dropdown with polygon layers from the project."""
        self.layer_combo.clear()
        project = QgsProject.instance()
        
        for layer_id, layer in project.mapLayers().items():
            if isinstance(layer, QgsVectorLayer):
                if layer.geometryType() == 2:  # Polygon geometry
                    self.layer_combo.addItem(layer.name(), layer_id)
        
        if self.layer_combo.count() == 0:
            QMessageBox.warning(
                self, 
                "No Layers Found", 
                "No polygon layers found in the current project."
            )
    
    def on_layer_changed(self, index):
        """Update field dropdowns when layer selection changes."""
        self.depth_field_combo.clear()
        self.ground_field_combo.clear()
        self.additional_field_combo.clear()
        
        layer = self.get_selected_layer()
        if layer is None:
            return
            
        # Populate field dropdowns with numeric fields
        for field in layer.fields():
            if field.type() in (QVariant.Double, QVariant.Int, QVariant.LongLong):
                field_name = field.name()
                self.depth_field_combo.addItem(field_name)
                self.ground_field_combo.addItem(field_name)
                self.additional_field_combo.addItem(field_name)
        
        # Try to set default values
        self._set_default_field(self.depth_field_combo, ['depth2d', 'depth', 'DEPTH2D', 'DEPTH'])
        self._set_default_field(self.ground_field_combo, ['gndlev2d', 'ground', 'GNDLEV2D', 'GROUND', 'elevation'])
    
    def _set_default_field(self, combo, defaults):
        """Set the combo box to a default value if found."""
        for default in defaults:
            # Case insensitive search
            index = combo.findText(default, Qt.MatchFixedString)
            if index >= 0:
                combo.setCurrentIndex(index)
                return
    
    def on_additional_field_toggled(self, state):
        """Enable/disable additional field based on checkbox."""
        self.additional_field_combo.setEnabled(state == 2)  # Qt.Checked = 2
    
    def browse_output_folder(self):
        """Open a dialog to select the output folder."""
        folder = QFileDialog.getExistingDirectory(
            self,
            "Select Output Folder",
            "",
            QFileDialog.ShowDirsOnly
        )
        if folder:
            self.output_folder_edit.setText(folder)
    
    def get_selected_layer(self):
        """Get the currently selected layer."""
        layer_id = self.layer_combo.currentData()
        if layer_id:
            return QgsProject.instance().mapLayer(layer_id)
        return None
    
    def get_parameters(self):
        """Get the dialog parameters."""
        return {
            'layer': self.get_selected_layer(),
            'depth_field': self.depth_field_combo.currentText(),
            'ground_field': self.ground_field_combo.currentText(),
            'additional_field': self.additional_field_combo.currentText() if self.use_additional_field.isChecked() else None,
            'resolution': self.resolution_spin.value(),
            'output_folder': self.output_folder_edit.text().strip() or None,
        }


class PolygonToTinProcessor:
    """Process polygon layer to multiple TIN meshes."""
    
    def __init__(self, params, feedback=None):
        self.params = params
        self.feedback = feedback or QgsProcessingFeedback()
        self.layer = params['layer']
        self.depth_field = params['depth_field']
        self.ground_field = params['ground_field']
        self.additional_field = params.get('additional_field')
        self.resolution = params['resolution']
        self.output_folder = params.get('output_folder')
        
        # Intermediate results
        self.prepared_layer = None
        self.centroid_layer = None
        self.vertex_layer = None
        self.created_tins = []
        
    def run(self):
        """Execute all processing steps to create multiple TIN outputs."""
        try:
            self.feedback.pushInfo("Starting 2D Zone to TIN conversion...")
            
            # Step 1: Prepare layer with calculated water surface field
            self.feedback.pushInfo("Step 1: Preparing layer with water surface calculation...")
            self.feedback.setProgress(5)
            self.prepare_layer()
            
            # Step 2: Extract centroids
            self.feedback.pushInfo("Step 2: Extracting centroids...")
            self.feedback.setProgress(10)
            self.extract_centroids()
            
            # Step 3: Extract vertices
            self.feedback.pushInfo("Step 3: Extracting vertices...")
            self.feedback.setProgress(15)
            self.extract_vertices()
            
            # Build list of TINs to create
            tin_configs = [
                {'field': self.depth_field, 'name': 'depth'},
                {'field': 'ws', 'name': 'water surface'},
            ]
            if self.additional_field:
                tin_configs.append({'field': self.additional_field, 'name': self.additional_field})
            
            # Calculate progress per TIN
            progress_start = 20
            progress_per_tin = (95 - progress_start) // len(tin_configs)
            
            # Create each TIN and add to project immediately
            for i, config in enumerate(tin_configs):
                tin_progress = progress_start + (i * progress_per_tin)
                self.feedback.pushInfo(f"\n{'=' * 50}")
                self.feedback.pushInfo(f"Creating TIN: {config['name']}")
                self.feedback.pushInfo(f"{'=' * 50}")
                self.feedback.setProgress(tin_progress)
                
                tin_path = self.create_tin_for_field(config['field'], config['name'])
                if tin_path:
                    # Add to project immediately to prevent temp file issues
                    self._add_tin_to_project(tin_path, config['name'])
                    self.created_tins.append({'name': config['name']})
                    self.feedback.pushInfo(f"Successfully created TIN: {config['name']}")
                else:
                    self.feedback.reportError(f"Failed to create TIN: {config['name']} for field: {config['field']}")
            
            self.feedback.setProgress(100)
            self.feedback.pushInfo("Processing complete!")
            
            # Return True only if at least one TIN was created
            if len(self.created_tins) > 0:
                return True
            else:
                self.feedback.reportError("No TIN meshes were created. Check the log for errors.")
                return False
            
        except Exception as e:
            self.feedback.reportError(f"Error during processing: {str(e)}")
            return False
    
    def prepare_layer(self):
        """Prepare layer with water surface field (ground + depth)."""
        # Calculate ws = ground + depth
        formula = f'"{self.ground_field}" + "{self.depth_field}"'
        result = processing.run("native:fieldcalculator", {
            'INPUT': self.layer,
            'FIELD_NAME': 'ws',
            'FIELD_TYPE': 0,  # Float
            'FIELD_LENGTH': 0,
            'FIELD_PRECISION': 0,
            'FORMULA': formula,
            'OUTPUT': 'TEMPORARY_OUTPUT'
        }, feedback=self.feedback)
        self.prepared_layer = result['OUTPUT']
    
    def extract_centroids(self):
        """Extract polygon centroids and save to a temp file for reliable reuse."""
        import tempfile
        import os
        
        # Create a temp file path for centroids
        temp_dir = tempfile.gettempdir()
        centroid_path = os.path.join(temp_dir, 'tin_centroids.gpkg')
        
        result = processing.run("native:centroids", {
            'INPUT': self.prepared_layer,
            'ALL_PARTS': False,
            'OUTPUT': centroid_path
        }, feedback=self.feedback)
        self.centroid_layer = result['OUTPUT']  # This will be the file path
        self.feedback.pushInfo(f"Centroids saved to: {self.centroid_layer}")
    
    def extract_vertices(self):
        """Extract vertices and remove duplicates, save to a temp file for reliable reuse."""
        import tempfile
        import os
        
        # Extract vertices
        result = processing.run("native:extractvertices", {
            'INPUT': self.prepared_layer,
            'OUTPUT': 'TEMPORARY_OUTPUT'
        }, feedback=self.feedback)
        vertex_layer = result['OUTPUT']
        
        # Remove duplicate geometries and save to temp file
        temp_dir = tempfile.gettempdir()
        vertex_path = os.path.join(temp_dir, 'tin_vertices.gpkg')
        
        result = processing.run("native:deleteduplicategeometries", {
            'INPUT': vertex_layer,
            'OUTPUT': vertex_path
        }, feedback=self.feedback)
        self.vertex_layer = result['OUTPUT']  # This will be the file path
        self.feedback.pushInfo(f"Vertices saved to: {self.vertex_layer}")
    
    def create_tin_for_field(self, field_name, output_name):
        """
        Create a TIN mesh for a specific field.
        
        This method runs the full TIN creation pipeline:
        1. Create TIN from centroids using the specified field
        2. Rasterize the TIN
        3. Drape vertices on raster
        4. Create final TIN from draped vertices
        
        Args:
            field_name: The field to use for Z values
            output_name: Name for the output TIN layer
            
        Returns:
            Path to the created TIN mesh, or None if failed
        """
        try:
            # Step A: Create TIN from centroids
            self.feedback.pushInfo(f"  Creating centroid TIN for field: {field_name}")
            centroid_tin = self._create_centroid_tin(field_name)
            if not centroid_tin:
                return None
            
            # Step B: Convert TIN to raster
            self.feedback.pushInfo(f"  Converting TIN to raster...")
            raster = self._tin_to_raster(centroid_tin, field_name)
            if not raster:
                return None
            
            # Step C: Drape vertices on raster
            self.feedback.pushInfo(f"  Draping vertices on raster...")
            draped_vertices = self._drape_vertices(raster)
            if not draped_vertices:
                return None
            
            # Step D: Create final TIN from draped vertices
            self.feedback.pushInfo(f"  Creating final TIN mesh...")
            final_tin = self._create_final_tin(draped_vertices, output_name)
            
            return final_tin
            
        except Exception as e:
            self.feedback.reportError(f"  Error creating TIN for {output_name}: {str(e)}")
            return None
    
    def _create_centroid_tin(self, field_name):
        """Create TIN mesh from centroids using specified field."""
        # Load centroid layer from saved file path
        centroid_layer = QgsVectorLayer(self.centroid_layer, f"centroids_{field_name}", "ogr")
        
        if not centroid_layer.isValid():
            self.feedback.reportError(f"  Failed to load centroid layer from: {self.centroid_layer}")
            return None
        
        # Add the layer to the project temporarily
        QgsProject.instance().addMapLayer(centroid_layer, False)
        
        layer_id = centroid_layer.id()
        field_index = centroid_layer.fields().indexOf(field_name)
        
        self.feedback.pushInfo(f"  Looking for field '{field_name}' in centroid layer")
        self.feedback.pushInfo(f"  Available fields: {[f.name() for f in centroid_layer.fields()]}")
        
        if field_index == -1:
            self.feedback.reportError(f"  Field '{field_name}' not found in centroid layer")
            QgsProject.instance().removeMapLayer(centroid_layer.id())
            return None
        
        self.feedback.pushInfo(f"  Found field at index: {field_index}")
        
        params = {
            'SOURCE_DATA': [{
                'source': layer_id,
                'type': 0,
                'attributeIndex': field_index
            }],
            'MESH_FORMAT': 0,
            'CRS_OUTPUT': None,
            'OUTPUT_MESH': 'TEMPORARY_OUTPUT'
        }
        
        result = processing.run("native:tinmeshcreation", params, feedback=self.feedback)
        QgsProject.instance().removeMapLayer(centroid_layer.id())
        
        return result['OUTPUT_MESH']
    
    def _tin_to_raster(self, tin_path, field_name):
        """Convert TIN mesh to raster for interpolation."""
        mesh_layer = QgsMeshLayer(tin_path, "centroid_tin", "mdal")
        
        if not mesh_layer.isValid():
            self.feedback.reportError("  Failed to load centroid TIN mesh")
            return self._fallback_idw_interpolation(field_name)
        
        extent = self.layer.extent()
        
        result = processing.run("native:meshrasterize", {
            'INPUT': mesh_layer,
            'DATASET_GROUPS': [0],
            'DATASET_TIME': {'type': 'static'},
            'EXTENT': extent,
            'PIXEL_SIZE': self.resolution,
            'CRS_OUTPUT': self.layer.crs(),
            'OUTPUT': 'TEMPORARY_OUTPUT'
        }, feedback=self.feedback)
        
        return result['OUTPUT']
    
    def _fallback_idw_interpolation(self, field_name):
        """Fallback method using IDW interpolation if mesh rasterization fails."""
        self.feedback.pushInfo("  Using IDW interpolation as fallback...")
        
        # Load centroid layer from saved file path
        centroid_layer = QgsVectorLayer(self.centroid_layer, "centroids_idw", "ogr")
        
        field_index = centroid_layer.fields().indexOf(field_name)
        extent = self.layer.extent()
        
        result = processing.run("qgis:idwinterpolation", {
            'INTERPOLATION_DATA': f'{centroid_layer.source()}::~::0::~::{field_index}::~::0',
            'DISTANCE_COEFFICIENT': 2,
            'EXTENT': extent,
            'PIXEL_SIZE': self.resolution,
            'OUTPUT': 'TEMPORARY_OUTPUT'
        }, feedback=self.feedback)
        
        return result['OUTPUT']
    
    def _drape_vertices(self, raster):
        """Drape vertices on the raster to get interpolated Z values."""
        if isinstance(raster, str):
            raster_layer = QgsRasterLayer(raster, "raster")
        else:
            raster_layer = raster
        
        # Use the vertex layer file path directly
        self.feedback.pushInfo(f"  Using vertex layer: {self.vertex_layer}")
        
        # Set Z values from raster
        result = processing.run("native:setzfromraster", {
            'INPUT': self.vertex_layer,
            'RASTER': raster_layer,
            'BAND': 1,
            'NODATA': 0,
            'SCALE': 1,
            'OFFSET': 0,
            'OUTPUT': 'TEMPORARY_OUTPUT'
        }, feedback=self.feedback)
        vertex_with_z = result['OUTPUT']
        
        # Extract Z values to attribute
        result = processing.run("native:extractzvalues", {
            'INPUT': vertex_with_z,
            'SUMMARIES': [0],
            'COLUMN_PREFIX': 'z_',
            'OUTPUT': 'TEMPORARY_OUTPUT'
        }, feedback=self.feedback)
        
        return result['OUTPUT']
    
    def _create_final_tin(self, draped_vertices, output_name):
        """Create final TIN mesh from draped vertices."""
        import os
        
        if isinstance(draped_vertices, str):
            vertex_layer = QgsVectorLayer(draped_vertices, "vertices_temp", "ogr")
        else:
            vertex_layer = draped_vertices
        
        QgsProject.instance().addMapLayer(vertex_layer, False)
        
        layer_id = vertex_layer.id()
        
        # Find the z_ field
        z_field_index = -1
        for i, field in enumerate(vertex_layer.fields()):
            if field.name().startswith('z_'):
                z_field_index = i
                break
        
        if z_field_index == -1:
            self.feedback.reportError("  Could not find Z value field in draped vertices")
            QgsProject.instance().removeMapLayer(vertex_layer.id())
            return None
        
        # Determine output path - save to folder if specified, otherwise use temp
        if self.output_folder:
            # Sanitize output name for filename (replace spaces with underscores)
            safe_name = output_name.replace(' ', '_').replace('/', '_').replace('\\', '_')
            output_path = os.path.join(self.output_folder, f"{safe_name}.2dm")
            self.feedback.pushInfo(f"  Saving TIN to: {output_path}")
        else:
            output_path = 'TEMPORARY_OUTPUT'
        
        params = {
            'SOURCE_DATA': [{
                'source': layer_id,
                'type': 0,
                'attributeIndex': z_field_index
            }],
            'MESH_FORMAT': 0,
            'CRS_OUTPUT': None,
            'OUTPUT_MESH': output_path
        }
        
        result = processing.run("native:tinmeshcreation", params, feedback=self.feedback)
        QgsProject.instance().removeMapLayer(vertex_layer.id())
        
        return result['OUTPUT_MESH']
    
    def _add_tin_to_project(self, tin_path, tin_name):
        """Add a single TIN mesh to the QGIS project immediately after creation."""
        if tin_path:
            mesh_layer = QgsMeshLayer(tin_path, tin_name, "mdal")
            if mesh_layer.isValid():
                QgsProject.instance().addMapLayer(mesh_layer)
                self.feedback.pushInfo(f"Added TIN mesh layer: {tin_name}")
            else:
                self.feedback.reportError(f"Failed to add TIN mesh '{tin_name}' - layer invalid")
        else:
            self.feedback.reportError(f"No TIN mesh was created for '{tin_name}'")


def run_polygon_to_tin():
    """Main entry point to run the Polygon to TIN conversion."""
    dialog = PolygonToTinDialog()
    
    if dialog.exec_():
        params = dialog.get_parameters()
        
        if params['layer'] is None:
            QMessageBox.critical(None, "Error", "Please select a valid layer.")
            return
        
        if not params['depth_field']:
            QMessageBox.critical(None, "Error", "Please select a depth field.")
            return
        
        if not params['ground_field']:
            QMessageBox.critical(None, "Error", "Please select a ground level field.")
            return
        
        if not params['output_folder']:
            QMessageBox.critical(None, "Error", "Please select an output folder to save the TIN files.")
            return
        
        # Validate output folder exists
        import os
        if not os.path.isdir(params['output_folder']):
            QMessageBox.critical(None, "Error", f"Output folder does not exist:\n{params['output_folder']}")
            return
        
        # Create feedback for progress
        feedback = QgsProcessingFeedback()
        
        # Run the processor
        processor = PolygonToTinProcessor(params, feedback)
        success = processor.run()
        
        if success:
            # Build message with created TINs
            tin_names = [t['name'] for t in processor.created_tins]
            tin_list = '\n- '.join(tin_names) if tin_names else 'None'
            QMessageBox.information(
                None, 
                "Success", 
                f"TIN meshes created successfully!\n\nSaved to: {params['output_folder']}\n\nCreated layers:\n- {tin_list}"
            )
        else:
            QMessageBox.warning(
                None, 
                "Warning", 
                "Processing completed with errors. Check the log for details."
            )


# Run the script when executed directly in QGIS Python Console
if __name__ == '__main__':
    run_polygon_to_tin()
else:
    # Also allow running via: exec(open('polygon_to_tin.py').read())
    run_polygon_to_tin()

