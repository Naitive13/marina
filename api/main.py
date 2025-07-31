from flask import Flask
from waitress import serve
from paste.translogger import TransLogger
import logging

logger = logging.getLogger("waitress")
logger.setLevel(logging.DEBUG)
app = Flask(__name__)


@app.route("/ping")
def hello_world():
    return "pong"


if __name__ == "__main__":
    serve(TransLogger(app, setup_console_handler=False))
