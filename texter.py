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


class WM_OT_textOp(bpy.types.Operator):
    bl_label = "Add Text"
    bl_idname = "wm.textop"
    
    text = bpy.props.StringProperty(name="Enter Text:")
    scale = bpy.props.FloatProperty(name = "Scale:",default=1)
    center = bpy.props.BoolProperty(name = "Center Origin",default = False)
    extrude = bpy.props.BoolProperty(name = "Extrude",default = False)
    extrudeAmount = bpy.props.FloatProperty(name = "Extrude Amount:",default=0.05)
    rotation = bpy.props.BoolProperty(name= "Z up", default= False)
    
    def execute(self,context):
        
        t = self.text
        s = self.scale
        c = self.center
        e = self.extrude
        ea = self.extrudeAmount
        r = self.rotation
        
        bpy.ops.object.text_add(enter_editmode=True, align='WORLD', location=(0, 0,0))
        bpy.ops.font.delete(type='PREVIOUS_WORD')
        bpy.ops.font.text_insert(text=t)
        bpy.ops.object.editmode_toggle()
        
        if c == True:
            bpy.context.object.data.align_x = 'CENTER'
            bpy.context.object.data.align_y = 'CENTER'
            
        if e == True:
            bpy.context.object.data.extrude = 0.12

        if r == True:
            bpy.context.object.rotation_euler[0] = 1.5708

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