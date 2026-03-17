import nuke
import os

# Get the folder where this tool is installed
tool_root = os.path.dirname(__file__)

# Add the tool root to the plugin path
nuke.pluginAddPath(tool_root)

print("DL NukeAutoLoader, built Mar 2026.")
print("Copyright (c) 2026 Danilo de Lucio.  All Rights Reserved.")

# Add icons folder
icons_path = os.path.join(tool_root, "icon")

if os.path.exists(icons_path):
    nuke.pluginAddPath(icons_path)