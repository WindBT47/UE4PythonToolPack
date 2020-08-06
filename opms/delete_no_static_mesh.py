import unreal

# instances of unreal classes
editor_level_lib = unreal.EditorLevelLibrary()
editor_filter_lib = unreal.EditorFilterLibrary()

# get all level actors
level_actors = editor_level_lib.get_all_level_actors()
static_mesh_actors = editor_filter_lib.by_class(level_actors, unreal.StaticMeshActor)
deleted = 0

for actor in static_mesh_actors:
    actor_name = actor.get_fname()

    # get the static mesh through the static mesh component
    actor_mesh_com = actor.static_mesh_component
    actor_mesh = actor_mesh_com.static_mesh
    is_valid_actor = actor_mesh != None

    # if mesh not valid
    if not is_valid_actor:
        actor.destroy_actor()
        deleted += 1
        unreal.log("The Mesh component of actor {} is invalid and has been deleted".format(actor_name))

unreal.log("{} actor has been deleted".format(deleted))