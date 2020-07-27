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


import os
import bpy
from bpy.types import Panel



bl_info = {
    "name" : "3d shapes",
    "author" : "Kishan Mistry",
    "description" : "Workflow to add 3d shapes in the blender viewport",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "View3D > Toolshelf > 3d shapes",
    "warning" : "",
    "category" : "Mesh"
}




#Class for the panel, derived from panel
class AddshapesPanel(Panel):
    bl_space_type = 'VIEW3D'
    bl_region_type = 'TOOLS'
    bl_label = 'Tools Tab Label'
    bl_context = 'objectmode'
    bl_catergory = 'Kishan Mistry'
    
    
        
    #Add User Interface Elements Here
    def draw(self,context):
        layout = self.layout
        layout.operator('mesh.primitive_cube_add', text='Add New Cube')
    
        
#Registering the addon
def register():
    bpy.utils.register_class(AddshapesPanel)
    

#Unregistering the addon
def unregister():
    bpy.utils.unregister_class(AddshapesPanel)
    
    
#Needed to run script in text editor
if __name__ == '__main__':
    register()
    