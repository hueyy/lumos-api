import models
class DeviceRepo:
    def __init__(self, database):
        self.database = database

    def get_devices(self):
        devices = self.database.child('devices').get().val()
        print(devices)
        devices = [
            models.Device(value['area_id'], key, value['name'], value['value'])
        for key,value in devices.items() if value is not None]
        return devices

    def patch_device(self, deviceID, newDevice):
        self.database.child('devices').child(deviceID).update(newDevice.toUpdateDict())
