import os
import pyrebase
from flask import Flask, jsonify
from flask_sockets import Sockets
from flask_cors import CORS

from werkzeug.serving import run_with_reloader
from werkzeug.debug import DebuggedApplication
from gevent import pywsgi, monkey
from geventwebsocket.handler import WebSocketHandler

from api.websocket_blueprint import construct_websocket_blueprint
from config import FIREBASE_CONFIG
from api.device_blueprint import construct_device_blueprint
from api.spell_blueprint import construct_spell_blueprint
from api.area_blueprint import construct_area_blueprint
from api.webhook_blueprint import construct_webhook_blueprint
from api.lumos_exception import LumosException

app = Flask(__name__)
app.url_map.strict_slashes = False

CORS(app)

monkey.patch_all()
app.debug = True

sockets = Sockets(app)

firebase = pyrebase.initialize_app(FIREBASE_CONFIG)
database = firebase.database()

app.register_blueprint(construct_device_blueprint(database))
app.register_blueprint(construct_spell_blueprint(database))
app.register_blueprint(construct_area_blueprint(database))
app.register_blueprint(construct_webhook_blueprint(database))

sockets.register_blueprint(construct_websocket_blueprint(database))


# lumos-web
@app.route('/', methods=['GET'])
def serve_lumos_web_index():
    return app.send_static_file('index.html')


@app.errorhandler(LumosException)
def handle_exception(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


def run_server():
    if app.debug:
        application = DebuggedApplication(app)
    else:
        application = app
    server = pywsgi.WSGIServer(("0.0.0.0", 5000), application, handler_class=WebSocketHandler)
    server.serve_forever()


if __name__ == '__main__':
    run_with_reloader(run_server)
