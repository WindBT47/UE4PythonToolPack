import unreal

# instances of unreal classes
editor_asset_lib = unreal.EditorAssetLibrary()
string_lib = unreal.StringLibrary()

# get all assets in source dir
source_dir = "/Game/"
include_subfolders = True
set_textures = 0

assets = editor_asset_lib.list_assets(source_dir, recursive = include_subfolders)
color_patterns = ["_ORM", "_OcclusionRoughnessMetallic","_Metallic","_Roughness","_Mask"]

for asset in assets:
    # for every asset check it against all the patterns
    for pattern in color_patterns:
        if string_lib.contains(asset, pattern):
            # load the asset, tunr off sRGB and set compression settings to TC_Mask
            asset_obj = editor_asset_lib.load_asset(asset)
            asset_obj.set_editor_property("sRGB",False)
            asset_obj.set_editor_property("CompressionSettings", unreal.TextureCompressionSettings.TC_MASKS)

            unreal.log("Setting TC_Masks and turning off sRGB for asset {}".format(asset))
            set_textures += 1
            break

unreal.log("Linear color for matching textures set for {} asset".format(set_textures))