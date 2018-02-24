from copy import copy
from flask import Blueprint, jsonify, request
from repos.device_repo import DeviceRepo
from models.device import Device


def construct_device_blueprint(database):
    device_blueprint = Blueprint(__name__, 'device', url_prefix='/devices')

    device_repo = DeviceRepo(database)

    @device_blueprint.route('/', methods=['GET'])
    def get_devices():
        return jsonify([device.toFullDict() for device in device_repo.get_devices()])

    @device_blueprint.route('/<deviceID>', methods=['PATCH', 'POST'])
    def patch_device(deviceID):
        assert(request.headers['Content-Type'] == 'application/json')
        updatedDevice = request.json
        f = Device().toFullDict()
        g = copy(f)
        for k in f:
            if k in updatedDevice:
                g[k] = updatedDevice[k]
        print("updating ", deviceID, " to ", g)
        device_repo.patch_device(deviceID, Device(**g))
        return "Success"

    return device_blueprint
