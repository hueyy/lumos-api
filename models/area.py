class Area:
    def __init__(self, id=None, name=None, icon=None):
        self.id = id
        self.name = name
        self.icon = icon

    def toFullDict(self):
        return {
            'id': self.id,
            'name': self.name,
            'icon': self.icon
        }

    def toUpdateDict(self):
        r = dict()
        s = self.toFullDict()
        for k, v in s.items():
            if v is not None:
                r[k] = v
        return r
