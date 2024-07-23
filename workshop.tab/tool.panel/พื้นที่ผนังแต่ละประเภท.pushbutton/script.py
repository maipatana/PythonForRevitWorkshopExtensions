# -*- coding: utf-8 -*-

from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, UnitUtils
### ถ้าเป็น Version 2021-
from Autodesk.Revit.DB import UnitTypeId
### ถ้าเป็น Version 2021+
### from Autodesk.Revit.DB import UnitTypeId
from Convertor import ConvertToSquareMeter

doc = __revit__.ActiveUIDocument.Document
app =  __revit__.Application
uidoc = __revit__.ActiveUIDocument


walls = FilteredElementCollector(doc)\
.OfCategory(BuiltInCategory.OST_Walls)\
.WhereElementIsNotElementType().ToElements()

data = {}

for wall in walls:
    area = wall.LookupParameter("Area").AsDouble()
    #print(doc.GetElement(wall.GetTypeId()).LookupParameter("Type Name").AsString())
    type_name = wall.LookupParameter("Family and Type").AsValueString()
    #print("{} {}".format(type_name, area))
    if type_name in list(data):
        data[type_name] += area
    else:
        data[type_name] = area

for name in list(data):
    print(name, ConvertToSquareMeter(data[name]))

