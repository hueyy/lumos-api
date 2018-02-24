class DeviceRepo:
    def __init__(self, database):
        self.database = database

    def get_devices(self):
        devices = self.database.child('devices').get().val()
        devices = list(filter(lambda d: d is not None, devices))
        return devices
