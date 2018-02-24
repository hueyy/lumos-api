from models.device import Device


class DeviceRepo:
    def __init__(self, database):
        self.database = database

    def get_devices(self):
        devices = self.database.child('devices').get()
        print(devices)
        devices = [
            Device(device.val()['area_id'], device.key(), device.val()['name'], device.val()['value'])
            for device in devices.each() if device.val() is not None]
        return devices

    def patch_device(self, deviceID, newDevice):
        self.database.child('devices').child(deviceID).update(newDevice.toUpdateDict())

    def get_device(self, deviceID):
        s = self.database.child('devices').child(deviceID).get().val()
        if s is None:
            return None
        else:
            return Device(s['area_id'], deviceID, s['name'], s['value'])
