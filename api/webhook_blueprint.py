'''
This does is not for CRUD of triggers (see spell instead)
It exposes webhooks that other (possibly external) services call
'''

from flask import Blueprint, jsonify, request
from repos.spell_repo import SpellRepo

from api.lumos_exception import LumosException


def construct_webhook_blueprint(database):
    webhook_blueprint = Blueprint(__name__, 'webhook', url_prefix='/webhook')
    spell_repo = SpellRepo(database)

    @webhook_blueprint.route('/clock', methods=['POST'])
    def handle_scheduler_webhook():  # example
        data = request.get_json()
        if "spell_id" not in data:
            raise LumosException(message="pls specify spell_id")
        spell_id = data.get('spell_id')
        result = spell_repo.execute_actions(spell_id)
        return jsonify(result)

    @webhook_blueprint.route('/weather', methods=['POST'])
    def handle_weather_webhook():
        return

    return webhook_blueprint
