bl_info = {
    "name": "DYNAPRIM",
    "author": "RoninDev",
    "version": (0, 0, 1),
    "blender": (2, 93, 3),
    "location": "View3D > Add > DynaPrim > DynaPrim Objects",
    "description": "Adds a primitive object with dynamic parameter.",
    "warning": "",
    "doc_url": "https://github.com/roninzerodev/Dynaprim",
    "category": "Add Mesh",
}


import bpy
from bpy import data as bpy_data
from .operators import register_operator,unregister_operator
from .menu import register_ui,unregister_ui


def register():
    register_operator()
    register_ui()
    

def unregister():
    unregister_operator()
    unregister_ui()