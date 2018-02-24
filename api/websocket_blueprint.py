from flask import Blueprint
from config import Globals


def construct_websocket_blueprint(database):
    websocket_blueprint = Blueprint(__name__, 'websocket', url_prefix='/websocket')

    @websocket_blueprint.route('/')
    def handle_socket(socket):
        Globals.WEBSOCKET = socket
        while not socket.closed:
            message = socket.receive()
            socket.send("received: " + message)
        return

    return websocket_blueprint
