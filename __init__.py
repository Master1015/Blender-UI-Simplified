# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Blender UI Simplified",
    "author" : "Master1015",
    "description" : "An addon to help you",
    "blender" : (2, 80, 0),
    "version" : (1, 0, 0),
    "location" : "View3D Toolbar > Object Adder",
    "warning" : "",
    "category" : "Add Mesh"
}



import bpy

    #This is the Main Panel 
class MainPanel(bpy.types.Panel):
    bl_label = "Object Adder"
    bl_idname = "PT_MainPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Object Adder'

    def draw(self, context):
        layout = self.layout
        layout.scale_y = 1.2


    #Operation to add basic meshes in blender 
        row = layout.row()
        row.label(text= "Add a 3d Mesh", icon= 'OBJECT_ORIGIN')
        row = layout.row()       
        row.operator("mesh.primitive_torus_add", icon='MESH_TORUS', text="Torus")
        row.operator("mesh.primitive_cone_add", icon='CONE', text="Cone") 
        row.operator("mesh.primitive_cube_add", icon= 'CUBE', text= "Cube")
        row.operator("mesh.primitive_uv_sphere_add", icon= 'SPHERE', text= "Sphere")
        row.operator("mesh.primitive_monkey_add", icon= 'MESH_MONKEY', text= "Suzanne")

        #Seperate space for the curves
        row = layout.row()
        row.label(text= "Add curves", icon='MOD_CURVE')
        row = layout.row()
        row.operator("curve.primitive_bezier_curve_add", icon= 'CURVE_BEZCURVE', text= "Bezier Curve")
        row.operator("curve.primitive_bezier_circle_add", icon= 'CURVE_BEZCIRCLE', text= "Bezier Circle")
    


    
    

    #This is Panel A the special selection panel
class PanelA(bpy.types.Panel):
    bl_label = "Modifications"
    bl_idname = "PT_PanelA"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Object Adder'
    bl_parent_id = 'PT_MainPanel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
    
        row = layout.row()
        row.label(text= "Select a Modification option", icon= 'COLOR_BLUE')
        row = layout.row()
        row.operator("object.shade_smooth", icon= 'MOD_SMOOTH', text= "Set Smooth Shading")
        row.operator("object.subdivision_set", icon= 'MOD_SUBSURF', text= "Add Subsurf")
        row = layout.row()
        row.operator("object.modifier_add", icon= 'MODIFIER')


    



#SettingsPanel(Panel B)
class SettingsPanel(bpy.types.Panel):
    bl_label = "Settings"
    bl_idname = "PT_PanelC"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Object Adder'
    bl_parent_id = 'PT_MainPanel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
    
        row = layout.row()
        row.label(text= "Select a Setting", icon= 'SETTINGS')
        row = layout.row()
        row.operator("wm.url_open", text="Report a bug", icon='SPHERE').url = "https://github.com/Master1015/Blender-UI-Simplified/issues"
        row.operator("wm.url_open", text="Documentation", icon='QUESTION').url = "https://github.com/Master1015/Blender-UI-Simplified"
        

    
    

    

    
    #Here we are Registering the Classes       
def register():
    bpy.utils.register_class(MainPanel)
    bpy.utils.register_class(PanelA)
    bpy.utils.register_class(SettingsPanel)




    #Here we are UnRegistering the Classes   
def unregister():
    bpy.utils.unregister_class(MainPanel)
    bpy.utils.unregister_class(PanelA)
    bpy.utils.unregister_class(SettingsPanel)


    #This is required in order for the script to run in the text editor   
if __name__ == "__main__":
    register()
                        


