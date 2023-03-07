import unreal

editor_util = unreal.EditorUtilityLibrary()
layer_sys = unreal.LayersSubsystem()
editor_filter = unreal.EditorFilterLibrary()

selected_assets = editor_util.get_selected_assets()
material = editor_filter.by_class(selected_assets, unreal.Material)

if len(material) < 1:
    unreal.log("You need to select a Material in order to assign it")
else:
    material = material[0]
    material_name = material.get_fname()

    actors = layer_sys.get_selected_actors()
    static_mesh_actos = editor_filter.by_class(actors, unreal.StaticMeshActor)

    for actor in static_mesh_actos:
        actor_name = actor.get_fname()
        actor_mesh_comp = actor.static_mesh_component
        actor_mesh_comp.set_material(0, material)

        unreal.log("Assigning Material {} to actor {}".format(material_name, actor_name))
