from models.area import Area


class AreaRepo:
    def __init__(self, database):
        self.database = database

    def get_areas(self):
        rawAreas = self.database.child('areas').get()
        areas = [
            Area(area.key(), area.val()['name'])
            for area in rawAreas.each() if area.val() is not None]
        return areas

    def patch_area(self, areaID, newArea):
        self.database.child('areas').child(areaID).update(newArea.toUpdateDict())
