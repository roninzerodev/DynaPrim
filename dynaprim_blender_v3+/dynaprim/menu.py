import bpy
from bpy.utils import(
    register_class as register,
    unregister_class as unregister
)


from .operators import (
    DYNA_OT_Add_Cube,
    DYNA_OT_Add_Cylinder,
    DYNA_OT_Add_Sphere,
    DYNA_OT_Add_Plane,
    DYNA_OT_Add_Cone,
    DYNA_OT_Add_Circle,
    DYNA_OT_Add_Icosphere,
    DYNA_OT_Collapse,
)

label={
    1:'Cube',
    2:'Cylinder',
    3:'Sphere',
    4:'Plane',
    5:'Cone',
    6:'Circle',
    7:'IcoSphere'
}

class DYNA_PT_Dynaprim(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "DynaPrim"
    bl_label = "Dynamic Primitive"
  
    def draw(self,context):
        layout=self.layout
        selected=context.selected_objects
        obj=context.active_object
        wire=context.space_data.overlay
        space=context.space_data
        if len(selected)==0:
            return
        if obj is not None:
            if 'DYNAPRIM_TYPE' not in obj:
                layout.label(text='Select DYNAPRIM')
            else:
                prim_type=obj['DYNAPRIM_TYPE']
                gm = context.active_object.modifiers.get(obj.name+'_mod')
                row=layout.row(align=True)
                row.label(text=label[prim_type]+':')
                row.prop(wire,'show_wireframes')
                if prim_type==3:
                    options=["Input_9","Input_7","Input_5"]
                    row=layout.row(align=True)
                    row.label(text='Radius')
                    sub = row.row()
                    sub.scale_x = 1.33
                    sub.prop(gm,f'["{options[0]}"]',text='')
                    row=layout.row(align=True)
                    row.label(text='Segments')
                    sub = row.row()
                    sub.scale_x = 1.33
                    sub.prop(gm,f'["{options[1]}"]',text='')
                    row=layout.row(align=True)
                    row.label(text='Rings')
                    sub = row.row()
                    sub.scale_x = 1.33
                    sub.prop(gm,f'["{options[2]}"]',text='')
                   
                    
                elif prim_type==1:
                    options=["Input_13","Input_15","Input_17","Input_7","Input_9","Input_11"]
                    box=layout.box()
                    row=box.row(align=True)
                    row.label(text='Width-X')
                    sub = row.row()
                    sub.scale_x = 1.33
                    sub.prop(gm,f'["{options[0]}"]',text='')
                    row=box.row(align=True)
                    row.label(text='Length-Y')
                    sub = row.row()
                    sub.scale_x = 1.33
                    sub.prop(gm,f'["{options[1]}"]',text='')
                    row=box.row(align=True)
                    row.label(text='Height-Z')
                    sub = row.row()
                    sub.scale_x = 1.33
                    sub.prop(gm,f'["{options[2]}"]',text='')
                    box=layout.box()
                    row=box.row(align=True)
                    row.label(text='X-Segment')
                    sub = row.row()
                    sub.scale_x = 1.33
                    sub.prop(gm,f'["{options[3]}"]',text='')
                    row=box.row(align=True)
                    row.label(text='Y-Segment')
                    sub = row.row()
                    sub.scale_x = 1.33
                    sub.prop(gm,f'["{options[4]}"]',text='')
                    row=box.row(align=True)
                    row.label(text='Z-Segment')
                    sub = row.row()
                    sub.scale_x = 1.33
                    sub.prop(gm,f'["{options[5]}"]',text='')

                elif prim_type==2:
                    options=["Input_5","Input_7","Input_9"]
                    box=layout.box()
                    row=box.row(align=True)
                    row.label(text='Segments')
                    sub = row.row()
                    sub.scale_x = 1.33
                    sub.prop(gm,f'["{options[0]}"]',text='')
                    row=box.row(align=True)
                    row.label(text='Radius')
                    sub = row.row()
                    sub.scale_x = 1.33
                    sub.prop(gm,f'["{options[1]}"]',text='')
                    row=box.row(align=True)
                    row.label(text='Depth')
                    sub = row.row()
                    sub.scale_x = 1.33
                    sub.prop(gm,f'["{options[2]}"]',text='')

                elif prim_type==4:
                    options=["Input_5","Input_7","Input_9","Input_11"]
                    box=layout.box()
                    row=box.row(align=True)
                    row.label(text='Size-X')
                    sub = row.row()
                    sub.scale_x = 1.33
                    sub.prop(gm,f'["{options[0]}"]',text='')
                    row=box.row(align=True)
                    row.label(text='Size-Y')
                    sub = row.row()
                    sub.scale_x = 1.33
                    sub.prop(gm,f'["{options[1]}"]',text='')
                    row=box.row(align=True)
                    row.label(text='X-Vertices')
                    sub = row.row()
                    sub.scale_x = 1.33
                    sub.prop(gm,f'["{options[2]}"]',text='')
                    row=box.row(align=True)
                    row.label(text='Y-Vertices')
                    sub = row.row()
                    sub.scale_x = 1.33
                    sub.prop(gm,f'["{options[3]}"]',text='')

                elif prim_type==5:
                    options=["Input_5","Input_7","Input_9","Input_11"]
                    box=layout.box()
                    row=box.row(align=True)
                    row.label(text='Vertices')
                    sub = row.row()
                    sub.scale_x = 1.33
                    sub.prop(gm,f'["{options[0]}"]',text='')
                    row=box.row(align=True)
                    row.label(text='Radius-Top')
                    sub = row.row()
                    sub.scale_x = 1.33
                    sub.prop(gm,f'["{options[1]}"]',text='')
                    row=box.row(align=True)
                    row.label(text='Radius-Bottom')
                    sub = row.row()
                    sub.scale_x = 1.33
                    sub.prop(gm,f'["{options[2]}"]',text='')
                    row=box.row(align=True)
                    row.label(text='Depth')
                    sub = row.row()
                    sub.scale_x = 1.33
                    sub.prop(gm,f'["{options[3]}"]',text='')

                elif prim_type==6:
                    options=["Input_5","Input_7"]
                    ng=bpy.data.node_groups["dynaprim_node_"+obj.name].nodes["Circle"]
                    box=layout.box()
                    row=box.row(align=True)
                    row.label(text='Vertices')
                    sub = row.row()
                    sub.scale_x = 1.33
                    sub.prop(gm,f'["{options[0]}"]',text='')
                    row=box.row(align=True)
                    row.label(text='Radius')
                    sub = row.row()
                    sub.scale_x = 1.33
                    sub.prop(gm,f'["{options[1]}"]',text='')
                    row=box.row(align=True)
                    row.label(text='Fill Type')
                    sub = row.row()
                    sub.scale_x = 1.33
                    sub.prop(ng,"fill_type",text='')
                    
                elif prim_type==7:
                    options=["Input_5","Input_7"]
                    box=layout.box()
                    row=box.row(align=True)
                    row.label(text='Radius')
                    sub = row.row()
                    sub.scale_x = 1.33
                    sub.prop(gm,f'["{options[0]}"]',text='')
                    row=box.row(align=True)
                    row.label(text='Subdivision')
                    sub = row.row()
                    sub.scale_x = 1.33
                    sub.prop(gm,f'["{options[1]}"]',text='')
                    
                op=layout.operator(DYNA_OT_Collapse.bl_idname,text='Convert To Mesh')
                op.mode=1
                op2=layout.operator(DYNA_OT_Collapse.bl_idname,text='Collapse all Mods')
                op2.mode=2
                
        
  
def add_dynaprim_menu(self,context):
    layout=self.layout
    layout.separator()
    layout.operator(DYNA_OT_Add_Plane.bl_idname,text='Dyna Plane',icon='MESH_PLANE')
    layout.operator(DYNA_OT_Add_Cube.bl_idname,text='Dyna Cube',icon='CUBE')
    layout.operator(DYNA_OT_Add_Cylinder.bl_idname,text='Dyna Cylinder',icon='MESH_CYLINDER')
    layout.operator(DYNA_OT_Add_Sphere.bl_idname,text='Dyna Sphere',icon='SPHERE')
    layout.operator(DYNA_OT_Add_Circle.bl_idname,text='Dyna Circle',icon='MESH_CIRCLE')
    layout.operator(DYNA_OT_Add_Cone.bl_idname,text='Dyna Cone',icon='MESH_CONE')
    layout.operator(DYNA_OT_Add_Icosphere.bl_idname,text='Dyna Icosphere',icon='MESH_ICOSPHERE')

classes=[
    DYNA_PT_Dynaprim,
]

def register_ui():
    for cls in classes:
        register(cls)
        bpy.types.VIEW3D_MT_mesh_add.append(add_dynaprim_menu)
    
        

def unregister_ui():
    for cls in reversed(classes):
        unregister(cls)
        bpy.types.VIEW3D_MT_mesh_add.remove(add_dynaprim_menu)

     