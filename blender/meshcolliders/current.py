import bpy

selected_objects = bpy.context.selected_objects

bpy.ops.object.select_all(action='DESELECT')

for obj in selected_objects:
    duplicate = obj.copy()
    duplicate.data = obj.data.copy()

    duplicate.name = obj.name + "-colonly"

    bpy.context.collection.objects.link(duplicate)

    duplicate.parent = obj
    duplicate.parent_type = 'OBJECT'
    duplicate.matrix_parent_inverse = obj.matrix_world.inverted()

    duplicate.hide_viewport = True

for obj in selected_objects:
    obj.select_set(True)

bpy.context.view_layer.objects.active = obj
