# NFS-BlackBox-Part-Naming-Blender-Add-on
![Image alt](https://github.com/CiPH3R-88/NFS-BlackBox-Part-Naming-Blender-Add-on/blob/68426621efae795d22a52f33e4bd65a5bc082554/src/nfsbb_bulk_rename.png)

NFS BlackBox Part Naming is a Blender add-on designed to automate part renaming for Need for Speed BlackBox asset workflows.

It applies correct naming rules for:

-   BASE parts
-   KIT00 parts
-   STYLE variants (or custom prefix variants)
-   Special BODY kit numbering

The add-on renames both:

-   Object Name
-   Object Data (Mesh) Name

This ensures export-safe naming without .001 issues.

Features

-   Auto uppercase enforcement
-   Live preview before applying
-   Special KIT00_BODY_A numbering rule
-   Default STYLE## prefix generation
-   Optional custom prefix support (e.g. CHATGPT##)
-   Strict naming validation
-   Selection count display
-   Undo support
-   Automatically clears First Object Name after apply
-   Renames object and mesh data together

## 🎬 Demo Video

▶️ [Watch the Bulk Rename Demo](https://github.com/CiPH3R-88/NFS-BlackBox-Part-Naming-Blender-Add-on/blob/e9f2ac6aa05be98c392eaa024f36abf43ab28f81/src/nfsbb_bulk_rename.mp4)

Installation

1.  Open Blender.

2.  Go to Edit → Preferences → Add-ons.

3.  Click Install…

4.  Select the file:

    nfs_blackbox_part_naming.py

    (Or install the packaged ZIP if distributed as a folder-based
    add-on.)

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

5.  Enter the exact name of the first object (must start with BASE or
    KIT00_).

6.  (Optional) Enable Preview Names to see results before applying.

7.  (Optional) Enable Custom Prefix to use a different prefix instead of
    STYLE.

8.  Click Apply Rename.

After a successful rename, the First Object Name field will
automatically clear.

Important

-   At least 2 objects must be selected.
-   First selected object must match the input name.
-   Input must start with:
    -   BASE
    -   or KIT00_
-   Custom prefix must not be empty when enabled.

Compatibility

-   Blender 4.0+
-   Designed for NFS BlackBox workflows
