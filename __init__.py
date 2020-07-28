import bpy
from bpy.types import Panel

class Add3dshapesPanel(Panel):
    bl_info = {
        "name" : "Add3dshapes",
        "author" : "Kishan Mistry",
        "description" : "Workflow to add 3d shapes",
        "blender" : (2, 83, 3,0),
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






