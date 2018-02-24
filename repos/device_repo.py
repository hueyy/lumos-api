import json

from api.lumos_exception import LumosException
from models.device import Device
from config import Globals


class DeviceRepo:
    # device positions
    ON = 'on'
    OFF = 'off'
    TOGGLE = 'toggle'

    def __init__(self, database):
        self.database = database

    def get_devices(self):
        devices = self.database.child('devices').get()
        devices = [
            Device(device.val()['area_id'], device.key(), device.val()['name'], device.val()['value'])
            for device in devices.each() if device.val() is not None]
        return devices

    def get_device(self, device_id):
        s = self.database.child('devices').child(device_id).get().val()
        if s is None:
            return None
        else:
            return Device(s['area_id'], device_id, s['name'], s['value'])

    def patch_device(self, device_id, new_device):
        self.database.child('devices').child(device_id).update(new_device.toUpdateDict())
        device = self.get_device(device_id)
        return device

    def set_device_position(self, device_id, position):
        device = self.get_device(device_id)
        if not device:
            raise LumosException(message="Invalid device id")
        if position not in [DeviceRepo.ON, DeviceRepo.OFF, DeviceRepo.TOGGLE]:
            raise LumosException(message="Invalid position specified")
        if position == DeviceRepo.TOGGLE: # handle toggle
            position = DeviceRepo.ON if device.get("position") == DeviceRepo.OFF else DeviceRepo.OFF
        action = {
            "device_mac": device.get('mac'),
            "position": position
        }
        ws = Globals.WEBSOCKET
        if ws and not ws.closed:
            ws.send(json.dumps(action))
            return True
        else:
            raise LumosException(message="No websocket connection with hub", status_code=500)

