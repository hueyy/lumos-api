from copy import copy
from flask import Blueprint, jsonify, request, abort

from api.lumos_exception import LumosException
from repos.device_repo import DeviceRepo
from models.device import Device


def construct_device_blueprint(database):
    device_blueprint = Blueprint(__name__, 'device', url_prefix='/devices')

    device_repo = DeviceRepo(database)

    @device_blueprint.route('/', methods=['GET'])
    def get_devices():
        return jsonify([device.toFullDict() for device in device_repo.get_devices()])

    @device_blueprint.route('/<device_id>', methods=['GET'])
    def get_device_by_id(device_id):
        device = device_repo.get_device(device_id)
        return jsonify(device.toFullDict())

    @device_blueprint.route('/<device_id>', methods=['PATCH', 'POST'])
    def patch_device(device_id):
        assert(request.headers['Content-Type'] == 'application/json')
        updated_device = request.json
        f = Device().toFullDict()
        g = copy(f)
        for k in f:
            if k in updated_device:
                g[k] = updated_device[k]
        print("updating ", device_id, " to ", g)
        device = device_repo.patch_device(device_id, Device(**g))
        return jsonify(device.toFullDict())

    @device_blueprint.route('/<device_id>/action', methods=['POST'])
    def act_on_device(device_id):
        data = request.get_json()
        if "position" not in data:
            raise LumosException(message="pls specify position")
        position = data.get('position')
        result = device_repo.set_device_position(device_id, position)
        if result:
            return jsonify({"message": "success"})
        else:
            abort(500)

    return device_blueprint
