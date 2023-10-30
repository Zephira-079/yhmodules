import bpy

def duplicate_objects_recursive(obj):
    if not obj.name.endswith("-colonly"):
        # Check if any child has a name ending with "-colonly"
        skip_parent = any(child.name.endswith("-colonly") for child in obj.children)

        if not skip_parent:
            duplicate = obj.copy()
            duplicate.data = obj.data.copy()
            duplicate.name = obj.name + "-colonly"
            bpy.context.collection.objects.link(duplicate)
            duplicate.parent = obj
            duplicate.parent_type = 'OBJECT'
            duplicate.matrix_parent_inverse = obj.matrix_world.inverted()
            duplicate.hide_viewport = True

        for child in obj.children:
            duplicate_objects_recursive(child)

selected_objects = bpy.context.selected_objects
bpy.ops.object.select_all(action='DESELECT')
for obj in selected_objects:
    duplicate_objects_recursive(obj)
for obj in selected_objects:
    obj.select_set(True)

# Set the last selected object as the active object
bpy.context.view_layer.objects.active = selected_objects[-1] if selected_objects else None
