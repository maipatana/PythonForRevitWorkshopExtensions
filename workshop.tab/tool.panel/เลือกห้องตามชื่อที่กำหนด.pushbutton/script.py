# -*- coding: utf-8 -*-

import clr
clr.AddReference("System")
from System.Collections.Generic import List

from Autodesk.Revit.DB import (
    FilteredElementCollector, 
    BuiltInCategory, 
    UnitUtils, 
    Transaction,
    ElementId
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

SELECTED_NAMES = ["Bed Room", "Living Room", "Dinning"]
selections = List[ElementId]()
for room in rooms:
    name = room.LookupParameter("Name").AsString()
    if name in SELECTED_NAMES:
        selections.Add(room.Id)
        ### เลือก Elements

uidoc.Selection.SetElementIds(selections)