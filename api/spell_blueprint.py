from flask import Blueprint, jsonify, request
from repos.spell_repo import SpellRepo
from api.lumos_exception import LumosException


def construct_spell_blueprint(database):
    spell_blueprint = Blueprint(__name__, 'spell', url_prefix='/spells')

    spell_repo = SpellRepo(database)

    @spell_blueprint.route('/', methods=['GET'])
    def get_spells():
        return jsonify(spell_repo.get_spells())

    @spell_blueprint.route('/<spell_id>', methods=['GET'])
    def get_spell_by_id(spell_id):
        spell = spell_repo.get_spell_by_id(spell_id)
        return jsonify(spell)

    @spell_blueprint.route('/', methods=['POST'])
    def create_spell():
        spell = spell_repo.create_spell()
        return jsonify(spell)

    @spell_blueprint.route('/<spell_id>/trigger', methods=['PUT'])
    def set_trigger(spell_id):
        data = request.get_json()
        if "trigger" not in data:
            raise LumosException(message="trigger not specified")
        trigger = data.get('trigger')
        spell = spell_repo.set_trigger(spell_id, trigger)
        return jsonify(spell)

    @spell_blueprint.route('/<spell_id>/action', methods=['PUT'])
    def set_action(spell_id):
        data = request.get_json()
        if "action" not in data:
            raise LumosException(message="action not specified")
        if "device_id" not in data.get('action') or "position" not in data.get('action'):
            raise LumosException(message="pls specify device_id & position")
        device_id = data.get('action').get('device_id')
        position = data.get('action').get('position')
        action_id = data.get('action').get('id')
        spell = spell_repo.set_action(spell_id, device_id, position, action_id=action_id)
        return jsonify(spell)

    @spell_blueprint.route('/<spell_id>/trigger', methods=['DELETE'])
    def delete_trigger(spell_id):
        spell = spell_repo.remove_trigger(spell_id)
        return jsonify(spell)

    @spell_blueprint.route('/<spell_id>/action/<action_id>', methods=['DELETE'])
    def delete_action(spell_id, action_id):
        spell = spell_repo.remove_action(spell_id, action_id)
        return jsonify(spell)

    @spell_blueprint.route('/<spell_id>/pullTrigger', methods=['POST', 'GET'])
    def pull_trigger(spell_id):
        print("i just got triggered by {}".format(spell_id))
        result = spell_repo.execute_actions(spell_id)
        if result:
            return jsonify({"message": "executed"})
        else:
            raise LumosException(message="Something went wrong when executing actions")

    return spell_blueprint
