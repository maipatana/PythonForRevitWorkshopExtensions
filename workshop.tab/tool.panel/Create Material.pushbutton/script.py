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
    UnitTypeId,
    Material,
    Color
    )

from Autodesk.Revit.UI import TaskDialog

doc = __revit__.ActiveUIDocument.Document
app =  __revit__.Application
uidoc = __revit__.ActiveUIDocument


MATERIAL_NAMES = [
    "Plain Red",
    "Plain Blue",
    "Plain Green",
    "Plain Yellow"
]

MATERIAL_COLORS = [
    (200,0,0),
    (0,0,200),
    (0,200,0),
    (200,200,0)
]


def GetMaterialByName(name):
    ## หา Materials ทั้งหมดในไฟล์
    materials = FilteredElementCollector(doc)\
        .OfCategory(BuiltInCategory.OST_Materials)\
            .WhereElementIsNotElementType()\
                .ToElements()
    for mat in materials:
        if mat.Name == name:
            return mat
    return None#doc.GetElement(Material.Create(doc, name))

t = Transaction(doc)
t.Start("Create Material")
for mat, color in zip(MATERIAL_NAMES, MATERIAL_COLORS):
    newmat = GetMaterialByName(mat)
    r = color[0]
    g = color[1]
    b = color[2]
    newmat.Color = Color(r,g,b)
t.Commit()