# -*- coding: utf-8 -*-

import os

import clr
clr.AddReference("System")
from System.Collections.Generic import List

from Autodesk.Revit.DB import (
    NavisworksExportOptions, 
    )

doc = __revit__.ActiveUIDocument.Document
app =  __revit__.Application
uidoc = __revit__.ActiveUIDocument

FOLDER = "C:\\Users\\User\\OneDrive - Architects 49 Limited\\Desktop\\testexportnwc"
#os.chdir(FOLDER)
files = os.listdir(FOLDER)

for file in files:
    if file.endswith(".rvt"):
        linkPath = FOLDER + "\\" + file
        file_doc = app.OpenDocumentFile(linkPath)
        file_doc.Export(FOLDER, file[:-4] + ".nwc", NavisworksExportOptions())
        file_doc.Close()

