import bpy

class TestPanel(bpy.types.Panel):
    bl_label = "Test Panel"
    bl_idname = "PT_TestPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Add Mesh"
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text = "Add an object", icon="CUBE")
        row = layout.row()
        row.operator("mesh.primitive_cube_add", icon="CUBE")
        row = layout.row()
        row.operator("mesh.primitive_uv_sphere_add", icon="SPHERE")
        row = layout.row()
        row.operator("mesh.primitive_plane_add", icon ="MESH_PLANE")
        row = layout.row()
        row.operator("mesh.primitive_circle_add", icon="MESH_CIRCLE")
        row = layout.row()
        row.operator("mesh.primitive_ico_sphere_add", icon="MESH_ICOSPHERE")
        row = layout.row()
        row.operator("mesh.primitive_cylinder_add", icon="MESH_CYLINDER")
        row = layout.row()
        row.operator("mesh.primitive_cone_add", icon="CONE")
        row = layout.row()
        row.operator("mesh.primitive_torus_add", icon="MESH_TORUS")
        
        
        
        
def register():
    bpy.utils.register_class(TestPanel)
    
def unregister():
    bpy.utils.unregister_class(TestPanel)
    


if __name__ == "__main__":
    register()