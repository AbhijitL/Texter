bl_info = {
    "name" : "Texter",
    "author" : "Abhijit Leihaorambam",
    "version" : (0, 1),
    "blender" : (2, 83, 0),
    "location" : "View3D > Tools",
    "warning" : "",
    "wiki_url" : "",
    "category" : "Add Text",
}


import bpy
import os

class Text_Panel(bpy.types.Panel):
    bl_label = "Texter"
    bl_idname = "PT_textPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Texter"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self,context):
        layout = self.layout

        row = layout.row()
        row.operator("wm.textop",icon="TEXT")
#enum property for text origin       
center_options = [
    ('CENTER', "Center", "Center text origin"),
    ('LEFT', "Left", "Left-align text origin"),
    ('RIGHT', "Right", "Right-align text origin"),
]

class WM_OT_textOp(bpy.types.Operator):
    bl_label = "Add Text"
    bl_idname = "wm.textop"

    text: bpy.props.StringProperty(name="Enter Text:")
    scale: bpy.props.FloatProperty(name="Scale", default=1.0)
    center: bpy.props.EnumProperty(
        name="Origin",
        items=center_options,
        default='CENTER',
        description="Set text origin alignment"
    )
    extrude: bpy.props.BoolProperty(name="Extrude", default=False)
    extrudeAmount: bpy.props.FloatProperty(name="Extrude Amount", default=0.05)
    rotation: bpy.props.BoolProperty(name="Z up", default=False)

    def execute(self, context):

        t = self.text
        s = self.scale
        origin = self.center
        c = self.center
        e = self.extrude
        ea = self.extrudeAmount
        r = self.rotation

        #create a new text data block
        text_data = bpy.data.curves.new("TextData", type='FONT')
        text_data.body = t

        #create a new object with the text data
        text_object = bpy.data.objects.new("TextObject", text_data)
        bpy.context.collection.objects.link(text_object)
        bpy.context.view_layer.objects.active = text_object
        text_object.location = (0, 0, 0)

        #set scale
        text_object.scale = (s, s, s)

        #set extrusion
        if e:
            text_data.extrude = ea

        #set rotation to upright 
        text_object.rotation_euler = (0, 0, 0)

        #handle origin alignment
        if origin == 'LEFT':
            text_object.data.align_x = 'LEFT'
        elif origin == 'RIGHT':
            text_object.data.align_x = 'RIGHT'
        else:  # 'CENTER' is the default
            text_object.data.align_x = 'CENTER'

        
        return {'FINISHED'}

    def invoke(self,context,event):
        return context.window_manager.invoke_props_dialog(self)




def register():
    bpy.utils.register_class(Text_Panel)
    bpy.utils.register_class(WM_OT_textOp)


def unregister():
    bpy.utils.unregister_class(Text_Panel)
    bpy.utils.unregister_class(WM_OT_textOp)


if __name__ == "__main__":
    register()
