# -*- coding: utf-8 -*-

from Autodesk.Revit.DB import (
    FilteredElementCollector, 
    BuiltInCategory, 
    UnitUtils, 
    Transaction
    )
### ถ้าเป็น Version 2021-
from Autodesk.Revit.DB import UnitTypeId
from Autodesk.Revit.UI import TaskDialog
### ถ้าเป็น Version 2021+
### from Autodesk.Revit.DB import UnitTypeId

doc = __revit__.ActiveUIDocument.Document
app =  __revit__.Application
uidoc = __revit__.ActiveUIDocument


rooms = FilteredElementCollector(doc)\
.OfCategory(BuiltInCategory.OST_Rooms)\
.WhereElementIsNotElementType().ToElements()

count = 0
delete_names = ""

t = Transaction(doc)
t.Start("Delete Rooms")
for room in rooms:
    name = room.LookupParameter("Name").AsString()
    if room.Area == 0 or room.Location == None:
        doc.Delete(room.Id)
        count += 1
        delete_names += name + "\n"
t.Commit()

dialog = TaskDialog("Purge Room")
dialog.MainInstruction = "สำเร็จ"
dialog.MainContent  = "ลบห้องไป {} ห้อง\n{}".format(count, delete_names)
dialog.Show()
