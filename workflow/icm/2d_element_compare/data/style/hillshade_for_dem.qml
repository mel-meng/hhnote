<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis styleCategories="Symbology" version="3.34.12-Prizren">
  <pipe-data-defined-properties>
    <Option type="Map">
      <Option type="QString" value="" name="name"/>
      <Option name="properties"/>
      <Option type="QString" value="collection" name="type"/>
    </Option>
  </pipe-data-defined-properties>
  <pipe>
    <provider>
      <resampling enabled="false" zoomedInResamplingMethod="bilinear" maxOversampling="2" zoomedOutResamplingMethod="bilinear"/>
    </provider>
    <rasterrenderer opacity="1" alphaBand="-1" multidirection="0" type="hillshade" zfactor="1" azimuth="315" angle="45" nodataColor="" band="1">
      <rasterTransparency/>
      <minMaxOrigin>
        <limits>None</limits>
        <extent>WholeRaster</extent>
        <statAccuracy>Estimated</statAccuracy>
        <cumulativeCutLower>0.02</cumulativeCutLower>
        <cumulativeCutUpper>0.98</cumulativeCutUpper>
        <stdDevFactor>2</stdDevFactor>
      </minMaxOrigin>
    </rasterrenderer>
    <brightnesscontrast brightness="0" contrast="0" gamma="1"/>
    <huesaturation colorizeGreen="128" colorizeOn="0" invertColors="0" colorizeStrength="100" colorizeBlue="128" grayscaleMode="0" saturation="0" colorizeRed="255"/>
    <rasterresampler zoomedOutResampler="bilinear" maxOversampling="2" zoomedInResampler="bilinear"/>
    <resamplingStage>resamplingFilter</resamplingStage>
  </pipe>
  <blendMode>0</blendMode>
</qgis>
