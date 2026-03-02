# NFS-BlackBox-Part-Naming-Blender-Add-on
NFS BlackBox Part Naming is a Blender add-on designed to automate part renaming for Need for Speed BlackBox asset workflows.

It applies correct naming rules for:

-   BASE parts
-   KIT00 parts
-   STYLE variants
-   Special BODY kit numbering

The add-on also renames both:

-   Object Name
-   Object Data (Mesh) Name

This ensures export-safe naming without .001 issues.

Features

-   Auto uppercase enforcement
-   Live preview before applying
-   Special KIT00_BODY_A numbering rule
-   STYLE## generation for non-body parts
-   Strict naming validation
-   Selection count display
-   Undo support
-   Renames object and mesh data together

Installation

1.  Open Blender.

2.  Go to Edit → Preferences → Add-ons.

3.  Click Install…

4.  Select the file:

    nfs_blackbox_part_naming.py

5.  Enable the checkbox:

    NFS BlackBox Part Naming

How To Use

1.  Place all parts inside one collection.

2.  Select the parts:

    -   Click the first object
    -   Shift + Click the last object

3.  Press N to open the Sidebar.

4.  Go to:

    NFS BB Bulk Rename

5.  Enter the exact name of the first object.

6.  (Optional) Enable Preview Names.

7.  Click Apply Rename.

Important

-   At least 2 objects must be selected.
-   First selected object must match the input name.
-   Input must start with:
    -   BASE
    -   or KIT00_

Compatibility

-   Blender 4.0+
-   Designed for NFS BlackBox workflows
