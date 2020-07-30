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
    "name": "Object Adder",
    "author": "Darkfall",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Toolbar > Object Adder",
    "description": "Adds objects and other functions to help our workflow (Tutorial Result)",
    "warning": "",
    "wiki_url": "",
    "category": "Add Mesh",
}

import bpy

    #This is the Main Panel (Parent of Panel A and B)
class MainPanel(bpy.types.Panel):
    bl_label = "Object Adder"
    bl_idname = "PT_MainPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Object Adder'
   
    def draw(self, context):
        layout = self.layout
        layout.scale_y = 1.2
       
        row = layout.row()
        row.label(text= "Add an object", icon= 'OBJECT_ORIGIN')
        row = layout.row()
        row.operator("mesh.primitive_cube_add", icon= 'CUBE', text= "Cube")
        row.operator("mesh.primitive_uv_sphere_add", icon= 'SPHERE', text= "Sphere")
        row.operator("mesh.primitive_monkey_add", icon= 'MESH_MONKEY', text= "Suzanne")
        row = layout.row()
        row.operator("curve.primitive_bezier_curve_add", icon= 'CURVE_BEZCURVE', text= "Bezier Curve")
        row.operator("curve.primitive_bezier_circle_add", icon= 'CURVE_BEZCIRCLE', text= "Bezier Circle")
       
       
        row = layout.row()
        row.operator("object.text_add", icon= 'FILE_FONT', text= "Add Font")
        row = layout.row()
       
       


    #This is Panel B - The Specials Sub Panel (Child of MainPanel)
class PanelA(bpy.types.Panel):
    bl_label = "Specials"
    bl_idname = "PT_PanelB"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Object Adder'
    bl_parent_id = 'PT_MainPanel'
    bl_options = {'DEFAULT_CLOSED'}
   
    def draw(self, context):
        layout = self.layout
       
        row = layout.row()
        row.label(text= "Select a Special Option", icon= 'COLOR_BLUE')
        row = layout.row()
        row.operator("object.shade_smooth", icon= 'MOD_SMOOTH', text= "Set Smooth Shading")
        row.operator("object.subdivision_set", icon= 'MOD_SUBSURF', text= "Add Subsurf")
        row = layout.row()
        row.operator("object.modifier_add", icon= 'MODIFIER')
       
  
       
    #Here we are Registering the Classes       
def register():
    bpy.utils.register_class(MainPanel)
    bpy.utils.register_class(PanelA)
   

    #Here we are UnRegistering the Classes   
def unregister():
    bpy.utils.unregister_class(MainPanel)
    bpy.utils.unregister_class(PanelA)
  

    #This is required in order for the script to run in the text editor   
if __name__ == "__main__":
    register()
                         
 
 
 
 
 
