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

class Add3dshapesPanel(Panel):
    bl_info = {
        "name" : "Add3dshapes",
        "author" : "Kishan Mistry",
        "description" : "",
        "blender" : (2, 80, 0),
        "version" : (0, 0, 1),
        "location" : "3D window toolshelf > Add3dshapes tab",
        "warning" : "",
        "category" : "Object"
    }


    #Add User Interface elements here
    def execute(self, context):
        layout = self.layout
        layout.operator("mesh.primitive_cube_add", text="Add cube")
        

#Registering the addon
def register():
    bpy.utils.register_class(Add3dshapesPanel)


#Unregisterin the addon
def unregister():
    bpy.utils.register_class(Add3dshapesPanel)


#Needed to run script
if __name__ == "__main__":
    register()






