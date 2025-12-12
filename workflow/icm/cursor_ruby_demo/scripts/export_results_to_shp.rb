# Export Simulation Results to Shapefile
# This script exports simulation results (nodes and links) to ESRI Shapefiles
# using the Open Data Export Center (ODEC).
#
# Prerequisites:
# - Simulation results must be open in GeoPlan
# - Configuration files (.cfg) for nodes and links must exist
#
# Usage:
# Run this script from the ICM UI with simulation results open

# Get the current network with results
net = WSApplication.current_network
db = WSApplication.current_database

if net.nil?
  puts "ERROR: No network is currently open."
  puts "Please open simulation results in GeoPlan and try again."
  return
end

# Determine the Run object for the opened results
# In ICM UI, when results are open, `net.model_object` may be either:
# - a Run model object, OR
# - a Sim model object whose parent is the Run
results_mo = net.model_object
if results_mo.nil?
  puts "ERROR: No results model object is associated with the currently open network."
  puts "Please open simulation results in GeoPlan and try again."
  return
end

run_object = nil
sim_object = nil

case results_mo.type
when 'Run'
  run_object = results_mo
when 'Sim'
  sim_object = results_mo
  if sim_object.parent_type.to_s == 'Run'
    run_object = db.model_object_from_type_and_id('Run', sim_object.parent_id)
  else
    puts "ERROR: Opened results are a Sim but parent is not a Run (parent_type=#{sim_object.parent_type})."
    return
  end
else
  puts "ERROR: Unexpected results model object type '#{results_mo.type}'. Expected 'Run' or 'Sim'."
  return
end

if run_object.nil?
  puts "ERROR: Could not determine run name from the opened results."
  puts "Please ensure the opened results are associated with a Run and try again."
  return
end

run_name = run_object.name.to_s
sim_name = sim_object&.name.to_s

puts "Run: #{run_name}"
puts "Simulation: #{sim_name}" unless sim_name.strip.empty?
puts "Exporting results using run name: #{run_name}"

# Default configuration and output folder
# Note: Keep defaults generic (no personal machine paths) so this script is shareable in a public repo.
default_folder =
  if ENV.key?('USERPROFILE') && !ENV['USERPROFILE'].to_s.strip.empty?
    File.join(ENV['USERPROFILE'], 'Desktop')
  else
    ''
  end

default_node_cfg = default_folder.empty? ? '' : File.join(default_folder, 'node.cfg')
default_link_cfg = default_folder.empty? ? '' : File.join(default_folder, 'link.cfg')

# Prompt user for configuration files and output folder
user_input = WSApplication.prompt "Export Simulation Results to Shapefile", [
  # Use an "open existing file" picker (not Save As) so the UI does not prompt to replace files.
  ['Node config file (.cfg)', 'String', default_node_cfg, nil, 'FILE', true, 'cfg', 'Configuration Files', false],
  ['Link config file (.cfg)', 'String', default_link_cfg, nil, 'FILE', true, 'cfg', 'Configuration Files', false],
  ['Output folder', 'String', default_folder, nil, 'FOLDER', 'Select output folder'],
  ['Prefix', 'String', run_name]
], false

# Check if user cancelled
if user_input.nil?
  puts "Export cancelled by user."
  return
end

node_cfg_file = user_input[0]
link_cfg_file = user_input[1]
output_folder = user_input[2]
prefix = user_input[3]

# Validate inputs
if node_cfg_file.nil? || node_cfg_file.strip.empty?
  puts "ERROR: Node configuration file path is required."
  return
end

if link_cfg_file.nil? || link_cfg_file.strip.empty?
  puts "ERROR: Link configuration file path is required."
  return
end

if output_folder.nil? || output_folder.strip.empty?
  puts "ERROR: Output folder is required."
  return
end

# Prefix (run name) for output filenames
if prefix.nil? || prefix.to_s.strip.empty?
  puts "ERROR: Prefix is required."
  return
end

# Check if config files exist
unless File.exist?(node_cfg_file)
  puts "ERROR: Node configuration file not found: #{node_cfg_file}"
  return
end

unless File.exist?(link_cfg_file)
  puts "ERROR: Link configuration file not found: #{link_cfg_file}"
  return
end

# Set ODEC export options
options = Hash.new
options['Error File'] = File.join(output_folder, 'export_errors.txt')

# Sanitize prefix for use in filenames (remove invalid characters)
safe_prefix = prefix.to_s.gsub(/[\\\/\:\*\?\"\<\>\|]/, '_').strip
if safe_prefix.empty?
  puts "ERROR: Prefix becomes empty after sanitization; please choose a different prefix."
  return
end

# Export Nodes to Shapefile
puts ""
puts "Exporting nodes..."
node_output_file = "#{safe_prefix}_node"

begin
  net.odec_export_ex(
    'SHP',                                    # Format: Shapefile
    node_cfg_file,                            # Configuration file path
    options,                                  # Export options
    'Node',                                   # Table to export
    File.join(output_folder, node_output_file) # Output file path (without extension)
  )
  puts "  Nodes exported to: #{File.join(output_folder, node_output_file)}.shp"
rescue => e
  puts "  ERROR exporting nodes: #{e.message}"
end

# Export Links (Conduits) to Shapefile
puts ""
puts "Exporting links..."
link_output_file = "#{safe_prefix}_link"

begin
  net.odec_export_ex(
    'SHP',                                    # Format: Shapefile
    link_cfg_file,                            # Configuration file path
    options,                                  # Export options
    'Conduit',                                # Table to export (All Links)
    File.join(output_folder, link_output_file) # Output file path (without extension)
  )
  puts "  Links exported to: #{File.join(output_folder, link_output_file)}.shp"
rescue => e
  puts "  ERROR exporting links: #{e.message}"
end

puts ""
puts "="*60
puts "Export complete!"
puts "Output folder: #{output_folder}"
puts "="*60

