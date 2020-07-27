
bl_info = {
    "name" : "Workflow to add 3d shapes",
    "author" : "Kishan Mistry",
    "description" : "This addon allows you to add 3d shapes to your viewport"
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "View3d",
    "warning" : "",
    "category" :"Generic"
    "tracker_url":"https://github.com/Master1015/Untitled/issues"
}

import bpy
from bpy.types import Panel

#Class for the panel, derived from panel
class AddshapesPanel(Panel):
    bl_space_type = 'View3d'
    bl_region_type = 'TOOLS'
    bl_label = 'Tools Tab Label'
    bl_context = 'objectmode'
    bl_catergory = 'Kishan Mistry'



    #Add User Interface Elements Here
    def draw(self.context):
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
