import os
import subprocess

from dotenv import load_dotenv
from flask import Flask, jsonify, request

load_dotenv()

FRANK_PATH = os.getenv("FRANK_PATH")

if FRANK_PATH is None:
    raise EnvironmentError("FRANK_PATH environment variable is not set")

app = Flask(__name__)


@app.route("/create", methods=["POST"])
def create():
    data = request.get_json()
    app.logger.info(f"Creating server based on {data}")
    return jsonify([{"port": start_frank()}]), 200


def start_frank() -> int:
    """
    Starts the game specified in FRANK_PATH
    TODO: Store the pid in a dict, so we can kill the server
    TODO: Get, or set the port under which the server should be reachable
    TODO: Somehow pass arguments to the game, e.g. lobby name, password...
    TODO: Return the port
    """
    p = subprocess.Popen([FRANK_PATH, "--headless"])  # type: ignore
    app.logger.info(f"Started frank with pid {p.pid}")
    return 0


if __name__ == "__main__":
    app.run()
