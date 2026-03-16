import nuke
import os

def load_gizmos(base_path, root_menu_name="Gizmos"):
    """
    Automatically loads gizmos from any folder structure.
    Supports:
    - loose gizmos in the root folder
    - subfolders as categories
    - multiple nested levels
    """

    base_path = os.path.normpath(base_path)

    if not os.path.exists(base_path):
        nuke.tprint("[DL AUTOLOADER] Path not found: " + base_path)
        return

    nuke.tprint("[DL AUTOLOADER] Loading gizmos from: " + base_path)

    # Create the root menu
    root_menu = nuke.menu("Nodes").addMenu(root_menu_name)

    # Walk through the entire folder structure
    for root, dirs, files in os.walk(base_path):

        # Relative path becomes the category name
        rel_path = os.path.relpath(root, base_path)

        # If in the root folder, do not create a subcategory
        if rel_path == ".":
            current_menu = root_menu
        else:
            category = rel_path.replace("\\", "/")
            current_menu = root_menu.addMenu(category)

        # Register all gizmos found
        for file in files:
            if file.endswith(".gizmo"):
                gizmo_name = os.path.splitext(file)[0]
                full_path = os.path.join(root, file).replace("\\", "/")

                # Add command to the menu
                current_menu.addCommand(
                    gizmo_name,
                    "nuke.createNode('{}')".format(gizmo_name)
                )

                # Add the folder to the plugin path
                nuke.pluginAddPath(root)

                nuke.tprint("[DL AUTOLOADER] Registered: {} ({})".format(gizmo_name, full_path))