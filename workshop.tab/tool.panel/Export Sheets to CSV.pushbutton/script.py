# -*- coding: utf-8 -*-

from datetime import date

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

sheets = FilteredElementCollector(doc)\
    .OfCategory(BuiltInCategory.OST_Sheets)\
        .WhereElementIsNotElementType()\
            .ToElements()

FOLDER = "C:\\Users\\User\\OneDrive - Architects 49 Limited\\Desktop\\"
year = date.today().year
month = '{:02d}'.format(date.today().month)
day = '{:02d}'.format(date.today().day)
day_name = "{}{}{}".format(year,month,day)
FILENAME = day_name + "_" +doc.PathName.split("\\")[-1][:-4] + ".csv"

data = ""
for sheet in sheets:
    if sheet.LookupParameter("Sheet Name") and sheet.LookupParameter("Sheet Number"):
        sheet_name = sheet.LookupParameter("Sheet Name").AsString()
        sheet_number = sheet.LookupParameter("Sheet Number").AsString()
        #print(sheet_name, sheet_number)
        data += "{},{}\n".format(sheet_number, sheet_name)
with open(FOLDER +FILENAME ,  "w") as wFile:
    wFile.write(data.encode("utf-8"))
