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


import bpy
from bpy.types import Panel

#Class for the panel derived by the panel
class Add3dshapes(Panel):
    bl_info = {
        "name" : "Add 3d shapes",
        "author" : "Kishan Mistry",
        "description" : "Workflow to add 3d shapes",
        "blender" : (2, 80, 0),
        "version" : (0, 0, 1),
        "location" : "3D window toolshelf > Add 3d shapes",
        "warning" : "",
        "category" : "Mesh"
    }


    #Add UI elements here
    def draw(self, context):
        layout = self.layout
        layout.operator("mesh.primitive_cube_add", text="Add New Cube")
 


#Registering the addon
def register():
    bpy.utils.register_class(Add3dshapes)

#Unregistering the addon
def unregister():
    bpy.utils.unregister_class(Add3dshapes)

#Needed to run the addon in blender
if __name__ == "__main__":
    register()
    