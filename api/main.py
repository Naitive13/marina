from flask import Flask, request
from waitress import serve
from paste.translogger import TransLogger
import logging
import os

logger = logging.getLogger("waitress")
logger.setLevel(logging.DEBUG)
app = Flask(__name__)


@app.route("/ping")
def pong():
    return "pong"


@app.route("/marina")
def marina():
    try:
        laza = request.args.get("laza")
        result = os.popen(f"../marina '{laza}'").read()
        if result == "":
            raise Exception("result is empty...")
        return result
    except Exception as e:
        app.logger.error(f"An error as occured: {e}")
        return f"Marina failed... \n {str(e)}"


if __name__ == "__main__":
    serve(TransLogger(app, setup_console_handler=False))
