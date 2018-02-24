class Device:
    def __init__(self, area_id=None, id=None, name=None, value=None):
        self.area_id = area_id
        self.id = id
        self.name = name
        self.value = value
    def toFullDict(self):
        return {
            'area_id': self.area_id, 
            'id': self.id, 
            'name': self.name, 
            'value': self.value
        }
    def toUpdateDict(self):
        r = dict()
        s = self.toFullDict()
        for k,v in s.items():
            if v is not None:
                r[k] = v
        return r
