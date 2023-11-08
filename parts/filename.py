import os
import FreeCAD as App
import Mesh

current_directory = os.getcwd()
fcstd_files = [file for file in os.listdir(current_directory) if file.endswith(".FCStd")]

for fcstd_file in fcstd_files:
    freecad_file_path = current_directory + "/" + fcstd_file

App.openDocument(freecad_file_path)

doc = App.ActiveDocument
parent_objects = [obj for obj in doc.Objects if obj.InList == []]
__objs__ = [obj for obj in parent_objects]

stl_file_path = current_directory + "/full_assembly.stl"
Mesh.export(__objs__, stl_file_path)

del __objs__
print("full_assembly.stl updated")
