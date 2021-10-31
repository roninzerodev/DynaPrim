import bpy
from bpy.utils import(
    register_class as register,
    unregister_class as unregister
)
import random

primtype={
    1:'cube',
    2:'cylinder',
    3:'sphere',
    4:'plane',
    5:'cone',
    6:'circle',
    7:'icosphere'
}
filepath=bpy.utils.user_resource('SCRIPTS',path='addons')+'\\dynaprim\\nodes.blend'

rand=random.randint(0, 100000)

def load_nodes():
    with bpy.data.libraries.load(filepath) as (data_from,data_to):
        dyna_nodes=[]
        for node in data_from.node_groups:
            if node not in bpy.data.node_groups:
                data_to.node_groups.append(node)
        bpy.context.scene['DYNAPRIM']=rand

def create_primitive(type):
    mesh=bpy.data.meshes.new(primtype[type])
    prim=bpy.data.objects.new(primtype[type],mesh)
    bpy.data.objects[prim.name].modifiers.new(prim.name+'_mod','NODES')

    old_mod=bpy.data.objects[prim.name].modifiers[0].node_group

    node_name=f'dynaprim_node_{primtype[type]}'
    bpy.data.objects[prim.name].modifiers[0].node_group=bpy.data.node_groups[node_name].copy()
    node=bpy.data.objects[prim.name].modifiers[0].node_group
    node.name= f'dynaprim_node_{prim.name}'
    
    prim.matrix_world=bpy.context.scene.cursor.matrix
    bpy.context.collection.objects.link(prim)
    prim['DYNAPRIM_TYPE']=type
    prim.select_set(True)
    bpy.context.view_layer.objects.active = prim

    bpy.data.node_groups.remove(old_mod)
    del old_mod

    bpy.context.space_data.overlay.show_wireframes = True

def create_dynaprim(context,type):
    if('DYNAPRIM' in context.scene and context.scene['DYNAPRIM']==rand):
            create_primitive(type)
    else:
        load_nodes()
        create_primitive(type)

class DYNA_OT_Load_Dynaprim_nodes(bpy.types.Operator):
    '''Loads dynaprim nodes to the scene'''
    bl_idname='dynaprim.load_nodes'
    bl_label='Load Dynaprim nodes'
    
    def execute(self,context):
        load_nodes()
        return {'FINISHED'}

class DYNA_OT_Add_Cylinder(bpy.types.Operator):
    '''Adds dynamic cylinder'''
    bl_idname='dynaprim.add_dyna_cylinder'
    bl_label='Add DynaCylinder'
    bl_options={'REGISTER','UNDO'}

    def execute(self,context):
        create_dynaprim(context,2)
        return {'FINISHED'}

class DYNA_OT_Add_Cube(bpy.types.Operator):
    '''Adds dynamic cube'''
    bl_idname='dynaprim.add_dyna_cube'
    bl_label='Add DynaCube'
    bl_options={'REGISTER','UNDO'}

    def execute(self,context):
        create_dynaprim(context,1)
        return {'FINISHED'}

class DYNA_OT_Add_Sphere(bpy.types.Operator):
    '''Adds dynamic sphere'''
    bl_idname='dynaprim.add_dyna_sphere'
    bl_label='Add Dynasphere'
    
    def execute(self,context):
        create_dynaprim(context,3)
        return {'FINISHED'}

class DYNA_OT_Add_Plane(bpy.types.Operator):
    '''Adds dynamic plane'''
    bl_idname='dynaprim.add_dyna_plane'
    bl_label='Add DynaPlane'
    
    def execute(self,context):
        create_dynaprim(context,4)
        return {'FINISHED'}

class DYNA_OT_Add_Cone(bpy.types.Operator):
    '''Adds dynamic cone'''
    bl_idname='dynaprim.add_dyna_cone'
    bl_label='Add DynaCone'
    
    def execute(self,context):
        create_dynaprim(context,5)
        return {'FINISHED'}

class DYNA_OT_Add_Circle(bpy.types.Operator):
    '''Adds dynamic circle'''
    bl_idname='dynaprim.add_dyna_circle'
    bl_label='Add DynaCircle'
    
    def execute(self,context):
        create_dynaprim(context,6)
        return {'FINISHED'}

class DYNA_OT_Add_Icosphere(bpy.types.Operator):
    '''Adds dynamic icosphere'''
    bl_idname='dynaprim.add_dyna_icosphere'
    bl_label='Add DynaIcosphere'
    
    def execute(self,context):
        create_dynaprim(context,7)
        return {'FINISHED'}

class DYNA_OT_Collapse(bpy.types.Operator):
    ''' Converts dynaprim to mesh by applying node modifier '''
    bl_idname='dynaprim.collapse_prim'
    bl_label='Collapse Geo'

    mode:bpy.props.IntProperty(default=1,min=1,max=2,name='mode')

    def execute(self,context):
        obj=context.active_object
        prim_type=obj['DYNAPRIM_TYPE']
        if(self.mode==1):
            bpy.ops.object.modifier_apply(modifier=obj.name+'_mod', report=True)
        if(self.mode==2):
            bpy.ops.object.convert(target='MESH')
        del obj['DYNAPRIM_TYPE']
        return {'FINISHED'}

  


classes=[
    DYNA_OT_Load_Dynaprim_nodes,
    DYNA_OT_Add_Cube,
    DYNA_OT_Add_Cylinder,
    DYNA_OT_Add_Sphere,
    DYNA_OT_Collapse,
    DYNA_OT_Add_Plane,
    DYNA_OT_Add_Icosphere,
    DYNA_OT_Add_Circle,
    DYNA_OT_Add_Cone
]

def register_operator():
    for cls in classes:
        register(cls)
    
        

def unregister_operator():
    for cls in reversed(classes):
        unregister(cls)
     

