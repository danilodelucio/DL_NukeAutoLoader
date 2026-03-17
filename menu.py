import nuke
import os
import json
import DL_NukeAutoLoader

tool_root = os.path.dirname(__file__)
config_path = os.path.join(tool_root, "custom_path.json")

default_gizmo_path = os.path.expanduser("~/.nuke/Gizmos")
gizmo_path = default_gizmo_path

if os.path.exists(config_path):
    try:
        with open(config_path, "r") as f:
            data = json.load(f)
            if "custom_path" in data and data["custom_path"].strip() != "":
                gizmo_path = data["custom_path"]
    except Exception as e:
        nuke.tprint("[DL NukeAutoLoader] Failed to read config:", e)


toolbar = nuke.toolbar("Nodes")
dl_menu = toolbar.addMenu("DL NukeAutoLoader", icon="tool.png")

dl_menu.addCommand(
    "Reload tools",
    "DL_NukeAutoLoader.load_gizmos(r'{}', root_menu=nuke.toolbar('Nodes').findItem('DL NukeAutoLoader'))".format(gizmo_path),
    icon="reload.png"
)

dl_menu.addSeparator()
DL_NukeAutoLoader.load_gizmos(gizmo_path, root_menu=dl_menu)