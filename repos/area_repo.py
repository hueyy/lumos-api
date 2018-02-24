from models.area import Area


class AreaRepo:
    def __init__(self, database):
        self.database = database

    def get_areas(self):
        raw_areas = self.database.child('areas').get()
        areas = [
            Area(area.key(), area.val()['name'], icon=area.val()['icon'])
            for area in raw_areas.each() if area.val() is not None]
        return areas

    def patch_area(self, area_id, new_area):
        self.database.child('areas').child(area_id).update(new_area.toUpdateDict())
