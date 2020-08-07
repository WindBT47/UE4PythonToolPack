import unreal

# instances of unreal classes
editor_asset_lib = unreal.EditorAssetLibrary()

# get all assets in source dir and option
source_dir = "/Game/Test"
include_subfolders = True
deleted = 0

# get all assets in source dir
assets = editor_asset_lib.list_assets(source_dir, recursive = include_subfolders, include_folder = True)
folders = [asset for asset in assets if editor_asset_lib.does_directory_exist(asset)]

for folder in folders:
    # check if folder has assets
    has_assets = editor_asset_lib.does_directory_have_assets(folder)

    if not has_assets:
        # delete fodler
        editor_asset_lib.delete_directory(folder)
        deleted += 1
        unreal.log("Folder {} without assets was deleted".format(folder))

unreal.log("Deleted {} folders without assets".format(deleted))