from flask import Blueprint, jsonify
from repos.device_repo import DeviceRepo


def construct_device_blueprint(database):
    device_blueprint = Blueprint(__name__, 'device', url_prefix='/device')

    device_repo = DeviceRepo(database)

    @device_blueprint.route('/', methods=['GET'])
    def get_devices():
        return jsonify(device_repo.get_devices())

    return device_blueprint
