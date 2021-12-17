bl_info = {
    "name" : "Object Adder",
    "author" : "Anuraag Saxena",
    "version" : (1, 0),
    "blender" : (2, 93, 6),
    "location" : "View3d > Tool",
    "warning" : "",
    "wiki_url" : "",
    "category" : "Add Mesh",
}




import bpy

class TestPanel(bpy.types.Panel):
    bl_label = "Object Adder"
    bl_idname = "PT_TestPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Add Mesh"
    bl_options = {"DEFAULT_CLOSED"}
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text = "Add an object", icon="OBJECT_ORIGIN")
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
        row = layout.row()
        row.operator("object.text_add", icon="FILE_FONT", text="Font Button")
        
     

class PanelA(bpy.types.Panel):
    bl_label = "Scaling"
    bl_idname = "PT_PanelA"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Add Mesh"
    bl_parent_id = "PT_TestPanel"
    bl_options = {"DEFAULT_CLOSED"}
    
    def draw(self, context):
        layout = self.layout
        obj = context.object
        
        row = layout.row()
        row.label(text = "Scale your object", icon="FONT_DATA")
        row = layout.row()
        row.operator("transform.resize")
        row = layout.row()
        col = layout.column()
        col.prop(obj, "scale")
#        layout.scale_y = 1.4

        
        
class PanelB(bpy.types.Panel):
    bl_label = "Specials"
    bl_idname = "PT_PanelB"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Add Mesh"
    bl_parent_id = "PT_TestPanel"
    bl_options = {"DEFAULT_CLOSED"}
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text = "Special Option", icon="COLOR_BLUE")
        row = layout.row()
        row.operator("object.shade_smooth")
#        row.operator("object.subdivision_set")
#        row.operator("object.modifier_add")

        
def register():
    bpy.utils.register_class(TestPanel)
    bpy.utils.register_class(PanelA)
    bpy.utils.register_class(PanelB)
    
    
def unregister():
    bpy.utils.unregister_class(TestPanel)
    bpy.utils.unregister_class(PanelA)
    bpy.utils.unregister_class(PanelB)


if __name__ == "__main__":
    register()