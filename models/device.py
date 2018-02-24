class Device:
    def __init__(self, area_id=None, id=None, name=None, position=None, mac=None):
        self.area_id = area_id
        self.id = id
        self.name = name
        self.position = position
        self.mac = mac

    def toFullDict(self):
        return {
            'area_id': self.area_id,
            'id': self.id,
            'name': self.name,
            'position': self.position,
            'mac': self.mac
        }

    def toUpdateDict(self):
        r = dict()
        s = self.toFullDict()
        for k, v in s.items():
            if v is not None:
                r[k] = v
        return r
