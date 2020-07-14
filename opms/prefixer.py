import unreal
import json

# instances of unreal classes
editor_util = unreal.EditorUtilityLibrary()
system_lib = unreal.SystemLibrary()

# prefix mapping
prefix_mapping = {}

with open("H:\\PythonProject\\opms\\prefix_mapping.json","r") as json_file:
    prefix_mapping = json.loads(json_file.read())

# get the selected assets
selected_assets = editor_util.get_selected_assets()
num_assets = len(selected_assets)
prefixed = 0

for asset in selected_assets:
    # get the class instance and the clear text name
    asset_name = system_lib.get_object_name(asset)
    asset_class = asset.get_class()
    class_name = system_lib.get_class_display_name(asset_class)

    # get the prefix for the given class
    class_prefix = prefix_mapping.get(class_name, None)

    if class_prefix is None:
        unreal.log_warning("No mapping for asset {} of type {}".format(asset_name, class_name))
        continue
    
    if not asset_name.startswith(class_prefix):
        # rename the asset and add prefix
        new_name = class_prefix + asset_name
        editor_util.rename_asset(asset, new_name)
        prefixed +=1
        unreal.log("Prefixed {} of type {} with{}".format(asset_name, class_name, new_name))

    else:
        unreal.log("Asset {} of type {} is already prefixed with".format(asset_name, class_name))

unreal.log("Prefixed {} of {} assets".format(prefixed, num_assets))