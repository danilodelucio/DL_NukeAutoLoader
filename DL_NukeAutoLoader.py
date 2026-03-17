# -----------------------------------------------------------------------------------
#  DL_NukeAutoLoader
#  Version: v01.0
#  Author: Danilo de Lucio
#  Website: www.danilodelucio.com
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
#  [Summary]
#  Automatically loads gizmos, Nuke files or Python scripts into the toolbar.
# -----------------------------------------------------------------------------------


import nuke
import os
import sys

SUPPORTED_EXT = [".gizmo", ".nk", ".nkind", ".py"]

ICON_GIZMO = "gizmo.png"
ICON_NUKE = "nuke.png"
ICON_FOLDER = "folder.png"
ICON_PYTHON = "python.png"


def scan_gizmos(root_path):
    categories = {}
    loose_items = []

    for root, dirs, files in os.walk(root_path):
        rel = os.path.relpath(root, root_path)

        if rel != ".":
            category_name = rel.replace("\\", "/")
            categories.setdefault(category_name, [])

        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in SUPPORTED_EXT:
                full_path = os.path.join(root, f)

                if rel == ".":
                    loose_items.append(full_path)
                else:
                    categories[category_name].append(full_path)

    return categories, loose_items


def get_icon_for_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".gizmo":
        return ICON_GIZMO
    if ext in [".nk", ".nkind"]:
        return ICON_NUKE
    if ext == ".py":
        return ICON_PYTHON

    return None


def add_item_to_menu(menu, file_path):
    name = os.path.splitext(os.path.basename(file_path))[0]
    ext = os.path.splitext(file_path)[1].lower()
    clean_path = file_path.replace("\\", "/")
    icon = get_icon_for_file(file_path)

    if ext == ".gizmo":
        menu.addCommand(
            name,
            "nuke.createNode('{}')".format(clean_path),
            icon=icon
        )

    elif ext in [".nk", ".nkind"]:
        menu.addCommand(
            name,
            "nuke.nodePaste('{}')".format(clean_path),
            icon=icon
        )

    elif ext == ".py":
        # Python 2 (Nuke <= 12) uses execfile
        # Python 3 (Nuke >= 13) uses exec(open().read())
        if sys.version_info[0] < 3:
            cmd = "execfile(r'{}')".format(clean_path)
        else:
            cmd = "exec(open(r'{}').read())".format(clean_path)

        menu.addCommand(
            name,
            cmd,
            icon=icon
        )


def load_gizmos(path, root_menu):
    if not os.path.exists(path):
        nuke.tprint("[DL NukeAutoLoader] Path not found: {}".format(path))
        return

    categories, loose_items = scan_gizmos(path)

    for category in sorted(categories.keys(), key=lambda s: s.lower()):
        cat_menu = root_menu.addMenu(category, icon=ICON_FOLDER)

        sorted_items = sorted(
            categories[category],
            key=lambda x: os.path.basename(x).lower()
        )

        for item in sorted_items:
            add_item_to_menu(cat_menu, item)

    sorted_loose = sorted(
        loose_items,
        key=lambda x: os.path.basename(x).lower()
    )

    for item in sorted_loose:
        add_item_to_menu(root_menu, item)