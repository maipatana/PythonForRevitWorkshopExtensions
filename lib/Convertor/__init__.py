from Autodesk.Revit.DB import UnitUtils, UnitTypeId

def ConvertToSquareMeter(number):
    return UnitUtils.ConvertFromInternalUnits(number, UnitTypeId.SquareMeters)

