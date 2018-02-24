class Area:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    def toFullDict(self):
        return {
            'id': self.id,
            'name': self.name
        }

    def toUpdateDict(self):
        r = dict()
        s = self.toFullDict()
        for k, v in s.items():
            if v is not None:
                r[k] = v
        return r
