import unreal


# Get editor utility library, layer subsystem, and filter library instances
editor_util = unreal.EditorUtilityLibrary()
layer_sys = unreal.LayersSubsystem()
editor_filter = unreal.EditorFilterLibrary()

# Get selected assets and filter for materials
selected_assets = editor_util.get_selected_assets()
material = editor_filter.by_class(selected_assets, unreal.Material)

if len(material) < 1:

    # If no materials are selected, log an error
    unreal.log("You need to select a Material in order to assign it")

else:

    # Get the first selected material
    material = material[0]
    material_name = material.get_fname()

    # Get selected actors and filter for static mesh actors
    actors = layer_sys.get_selected_actors()
    static_mesh_actos = editor_filter.by_class(actors, unreal.StaticMeshActor)

    for actor in static_mesh_actos:
        # Get the actor name and its static mesh component
        actor_name = actor.get_fname()
        actor_mesh_comp = actor.static_mesh_component
        # Set the first material slot to the selected material
        actor_mesh_comp.set_material(0, material)

        # Log a message for each actor that the material was assigned to
        unreal.log("Assigning Material {} to actor {}".format(material_name, actor_name))
