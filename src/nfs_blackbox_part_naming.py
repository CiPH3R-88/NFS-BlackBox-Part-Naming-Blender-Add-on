bl_info = {
    "name": "NFS BlackBox Part Naming",
    "author": "CIPHER_nfs",
    "version": (1, 1),
    "blender": (4, 0, 0),
    "location": "View3D > Sidebar > NFS BB Bulk Rename",
    "description": "Bulk rename parts for NFS BlackBox pipeline",
    "category": "Object",
}

import bpy


# -----------------------------
# Utility: Generate Name List
# -----------------------------

def generate_names(base_input, selected_objects, prefix):
    base_input = base_input.upper().strip()
    prefix = prefix.upper().strip()
    selected_objects = sorted(selected_objects, key=lambda o: o.name)

    new_names = []

    # Special BODY rule
    if base_input == "KIT00_BODY_A":
        for index, obj in enumerate(selected_objects):
            new_name = f"KIT{index:02d}_BODY_A"
            new_names.append((obj, new_name))
        return new_names

    # Extract suffix
    suffix = base_input
    if base_input.startswith("KIT00_"):
        suffix = base_input.replace("KIT00_", "", 1)

    for index, obj in enumerate(selected_objects):
        if index == 0:
            new_name = base_input
        else:
            new_name = f"{prefix}{index:02d}_{suffix}"
        new_names.append((obj, new_name))

    return new_names


# -----------------------------
# Operator
# -----------------------------

class OBJECT_OT_nfs_blackbox_rename(bpy.types.Operator):
    bl_idname = "object.nfs_blackbox_rename"
    bl_label = "Apply Rename"
    bl_description = "Rename selected parts using NFS BlackBox naming rules"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        props = context.scene.nfs_rename_props
        base_input = props.base_name.upper().strip()
        selected_objects = context.selected_objects

        if len(selected_objects) <= 1:
            self.report({'ERROR'}, "Select at least 2 valid part objects")
            return {'CANCELLED'}

        if not base_input:
            self.report({'ERROR'}, "First Object Name is empty")
            return {'CANCELLED'}

        if not (base_input.startswith("BASE") or base_input.startswith("KIT00_")):
            self.report({'ERROR'}, "Name must start with BASE or KIT00_")
            return {'CANCELLED'}

        selected_objects = sorted(selected_objects, key=lambda o: o.name)

        first_obj_name = selected_objects[0].name.upper()
        if first_obj_name != base_input:
            self.report({'ERROR'}, "First selected object does not match input name")
            return {'CANCELLED'}

        # Determine prefix
        prefix = "STYLE"
        if props.use_custom_prefix:
            if not props.custom_prefix.strip():
                self.report({'ERROR'}, "Custom prefix is empty")
                return {'CANCELLED'}
            prefix = props.custom_prefix

        name_pairs = generate_names(base_input, selected_objects, prefix)

        for obj, new_name in name_pairs:
            obj.name = new_name
            if obj.type == 'MESH':
                obj.data.name = new_name

        # Reset input after success
        props.base_name = ""

        self.report({'INFO'}, f"{len(selected_objects)} parts renamed successfully")
        return {'FINISHED'}


# -----------------------------
# Properties
# -----------------------------

class NFSRenameProperties(bpy.types.PropertyGroup):
    base_name: bpy.props.StringProperty(
        name="First Object Name",
        description="Example: BASE_A or KIT00_SPOILER_A",
        default=""
    )

    preview_mode: bpy.props.BoolProperty(
        name="Preview Names",
        default=True
    )

    use_custom_prefix: bpy.props.BoolProperty(
        name="Enable Custom Prefix",
        default=False
    )

    custom_prefix: bpy.props.StringProperty(
        name="Prefix",
        description="Example: STYLE or CHATGPT",
        default="STYLE"
    )


# -----------------------------
# UI Panel
# -----------------------------

class VIEW3D_PT_nfs_blackbox_panel(bpy.types.Panel):
    bl_label = "NFS BlackBox Part Naming"
    bl_idname = "VIEW3D_PT_nfs_blackbox_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "NFS BB Bulk Rename"

    def draw(self, context):
        layout = self.layout
        props = context.scene.nfs_rename_props
        selected_objects = context.selected_objects
        selected_count = len(selected_objects)

        layout.label(text="First Object Name")
        layout.prop(props, "base_name", text="")

        row = layout.row()
        row.enabled = False
        row.label(text=f"Selected Parts: {selected_count}")

        layout.separator()
        layout.prop(props, "use_custom_prefix")

        if props.use_custom_prefix:
            layout.prop(props, "custom_prefix")

        layout.prop(props, "preview_mode")
        layout.separator()

        base_input = props.base_name.upper().strip()

        valid = (
            selected_count > 1 and
            base_input and
            (base_input.startswith("BASE") or base_input.startswith("KIT00_"))
        )

        if props.preview_mode and valid:
            box = layout.box()
            box.label(text="Preview:")

            prefix = props.custom_prefix if props.use_custom_prefix else "STYLE"
            name_pairs = generate_names(base_input, selected_objects, prefix)

            for obj, new_name in name_pairs:
                box.label(text=new_name)

        layout.separator()
        layout.operator("object.nfs_blackbox_rename", icon='OUTLINER_OB_MESH')


# -----------------------------
# Register
# -----------------------------

classes = (
    OBJECT_OT_nfs_blackbox_rename,
    NFSRenameProperties,
    VIEW3D_PT_nfs_blackbox_panel,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.nfs_rename_props = bpy.props.PointerProperty(type=NFSRenameProperties)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.nfs_rename_props


if __name__ == "__main__":
    register()