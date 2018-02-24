from flask import Blueprint, jsonify
from repos.spell_repo import SpellRepo


def construct_spell_blueprint(database):
    spell_blueprint = Blueprint(__name__, 'spell', url_prefix='/spell')

    spell_repo = SpellRepo(database)

    @spell_blueprint.route('/', methods=['GET'])
    def get_devices():
        return jsonify(spell_repo.get_spells())

    @spell_blueprint.route('/<spell_id>', methods=['GET'])
    def get_device_by_id(spell_id):
        spell = spell_repo.get_spell_by_id(spell_id)
        return jsonify(spell)

    @spell_blueprint.route('/<spell_id>/trigger', methods=['DELETE'])
    def delete_trigger(spell_id):
        spell = spell_repo.remove_trigger(spell_id)
        return jsonify(spell)

    @spell_blueprint.route('/<spell_id>/action/<action_id>', methods=['DELETE'])
    def delete_action(spell_id, action_id):
        spell = spell_repo.remove_action(spell_id, action_id)
        return jsonify(spell)



    return spell_blueprint
