# -*- coding: utf-8 -*-

import clr
clr.AddReference("System")
from System.Collections.Generic import List

from Autodesk.Revit.DB import (
    FilteredElementCollector, 
    BuiltInCategory, 
    UnitUtils, 
    Transaction,
    ElementId,
    Wall,
    UnitTypeId
    )

from Autodesk.Revit.UI import TaskDialog

doc = __revit__.ActiveUIDocument.Document
app =  __revit__.Application
uidoc = __revit__.ActiveUIDocument

## หา Lines ทั้งหมดในไฟล์
lines = FilteredElementCollector(doc)\
    .OfCategory(BuiltInCategory.OST_Lines)\
        .WhereElementIsNotElementType()\
            .ToElements()


def GetWallTypeByName(wall_type_name):
    ### ----------------- เลือก Wall Type -------------------- ###
    wall_types = FilteredElementCollector(doc)\
    .OfCategory(BuiltInCategory.OST_Walls)\
        .WhereElementIsElementType()\
            .ToElements()
    for wall_type in wall_types:
        name = wall_type.LookupParameter("Type Name").AsString() ## ชื่อ Wall Type
        if name == wall_type_name: ## เช็คชื่อ
            return wall_type ## Retuen ค่า
    return None

selected_wall_type = GetWallTypeByName("Generic - 200mm")


def GetLevelByName(level_name):
    ### ----------------- เลือก Level -------------------- ###
    levels = FilteredElementCollector(doc)\
    .OfCategory(BuiltInCategory.OST_Levels)\
        .WhereElementIsNotElementType()\
            .ToElements() 
    for level in levels: ## Loop ทุก Level
        if level.Name == level_name: ## หา Level ที่ชื่อตรงกับที่ต้องการ
            return level ## Return ค่า
    return None

selected_level = GetLevelByName("Level 1") 



selections = []
selectionIds = uidoc.Selection.GetElementIds()
for elementid in selectionIds:
    element = doc.GetElement(elementid)
    selections.append(element)


t = Transaction(doc)
t.Start("Create Wall from Lines")
for line in selections:
    Wall.Create(
        doc, ## Document
        line.Location.Curve, ## Curve
        selected_wall_type.Id, ## Wall Type Id
        selected_level.Id, ## Level Id
        UnitUtils.ConvertToInternalUnits(5, UnitTypeId.Meters), ## Height
        0, ## Offset
        False, ## Boolean
        False ## Boolean
        )
t.Commit()


