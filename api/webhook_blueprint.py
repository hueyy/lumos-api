'''
This does is not for CRUD of triggers (see spell instead)
It exposes webhooks that other (possibly external) services call
'''

from flask import Blueprint, jsonify


def construct_webhook_blueprint(database):
    webhook_blueprint = Blueprint(__name__, 'webhook', url_prefix='/webhook')

    @webhook_blueprint.route('/clock', methods=['POST'])
    def handle_clock_webhook():  # example
        return

    @webhook_blueprint.route('/weather', methods=['POST'])
    def handle_weather_webhook():
        return
