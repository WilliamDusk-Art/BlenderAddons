
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Shapekey Copy",
    "blender": (2, 80, 0),
    "category": "Tool",
    "author": "Blender Bob, Chat GPT",    
}

import bpy

class ShapekeyTransferPanel(bpy.types.Panel):
    bl_label = "Shapekeys Copy"
    bl_idname = "PT_ShapekeyTransfer"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'

    def draw(self, context):
        layout = self.layout

        layout.prop_search(context.scene, "shapekey_source", context.scene, "objects", text="Source")
        layout.prop_search(context.scene, "shapekey_target", context.scene, "objects", text="Target")
        layout.operator("object.shapekey_transfer", text="Copy")

class ShapekeyTransferOperator(bpy.types.Operator):
    bl_idname = "object.shapekey_transfer"
    bl_label = "Transfer Shapekeys"
    bl_description = "Transfer shapekeys from source to target object"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        source_object = context.scene.shapekey_source
        target_object = context.scene.shapekey_target

        if source_object is None or target_object is None:
            self.report({'ERROR'}, "Please select both source and target objects.")
            return {'CANCELLED'}

        # Check if the source object has shape keys
        if not source_object.data.shape_keys:
            self.report({'ERROR'}, f"'{source_object.name}' does not have shape keys.")
            return {'CANCELLED'}

        # Create shape keys on the target object to match those on the source object
        for key in source_object.data.shape_keys.key_blocks:
            if target_object.data.shape_keys is None:
                bpy.ops.object.shape_key_add(from_mix=False)

            # Check if the shape key already exists on the target object
            if key.name not in target_object.data.shape_keys.key_blocks:
                target_object.shape_key_add(name=key.name)

            # Set the value of the shape key to 1
            target_object.data.shape_keys.key_blocks[key.name].value = 1.0

            # Copy vertex positions from source object's shape key to target object's shape key
            for idx, (vert_src, vert_tgt) in enumerate(zip(key.data, target_object.data.shape_keys.key_blocks[key.name].data)):
                vert_tgt.co = vert_src.co

        # Set the values of all shape keys on the target object to 0
        for key in target_object.data.shape_keys.key_blocks:
            key.value = 0.0

        self.report({'INFO'}, f"Shape keys copied from '{source_object.name}' to '{target_object.name}'. All shape key values set to 0.")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(ShapekeyTransferPanel)
    bpy.utils.register_class(ShapekeyTransferOperator)
    bpy.types.Scene.shapekey_source = bpy.props.PointerProperty(type=bpy.types.Object, name="Source Object")
    bpy.types.Scene.shapekey_target = bpy.props.PointerProperty(type=bpy.types.Object, name="Target Object")

def unregister():
    bpy.utils.unregister_class(ShapekeyTransferPanel)
    bpy.utils.unregister_class(ShapekeyTransferOperator)
    del bpy.types.Scene.shapekey_source
    del bpy.types.Scene.shapekey_target

if __name__ == "__main__":
    register()
