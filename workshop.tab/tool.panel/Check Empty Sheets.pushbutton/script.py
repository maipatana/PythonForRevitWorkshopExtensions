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

from Autodesk.Revit.UI import TaskDialog

doc = __revit__.ActiveUIDocument.Document
app =  __revit__.Application
uidoc = __revit__.ActiveUIDocument

views = FilteredElementCollector(doc)\
    .OfCategory(BuiltInCategory.OST_Views)\
        .WhereElementIsNotElementType()\
            .ToElements()

sheets = FilteredElementCollector(doc)\
    .OfCategory(BuiltInCategory.OST_Sheets)\
        .WhereElementIsNotElementType()\
            .ToElements()

sheet_numbers = []
for view in views:
    if view.LookupParameter("Sheet Number"):
        sheet_number = view.LookupParameter("Sheet Number").AsString()
        sheet_numbers.append(sheet_number)
print(sheet_numbers)

result = ""

for sheet in sheets:
    sheet_number = sheet.LookupParameter("Sheet Number").AsString()
    if sheet_number not in sheet_numbers:
        result += sheet_number + "\n"

mainDialog = TaskDialog("Check Empty Sheet")
mainDialog.MainContent = result
mainDialog.Show()

# ได้ผลเหมือนกัน
# for sheet in sheets:
#     sheet_number = sheet.LookupParameter("Sheet Number").AsString()
#     if len(sheet.GetAllViewports()) == 0:
#         print(sheet_number)