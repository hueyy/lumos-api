from copy import copy
from flask import Blueprint, jsonify, request
from repos.device_repo import DeviceRepo
import models
def foo():
    pass

def construct_action_blueprint(database):
    action_blueprint = Blueprint(__name__, 'action', url_prefix='/action')

    device_repo = DeviceRepo(database)

    @action_blueprint.route('/', methods=['POST'])
    def activate_device():
        print("i'm good ")
        assert(request.headers['Content-Type'] == 'application/json')
        actionData = request.json
        deviceID = actionData['device_id']
        action = actionData['action']

        #verify device existence
        if device_repo.get_device(deviceID) is None:
            return "Failure. Invalid deviceID {}".format(deviceID)

        actionMapping = {
            'on': lambda: foo(),
            'off': lambda: foo(),
            'toggle': lambda: foo()
        }
        if action in actionMapping:
            actionMapping[action]
            return "Success"
        else:
            return "Failure. Invalid action."

    return action_blueprint
