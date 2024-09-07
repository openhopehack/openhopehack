#!/usr/bin/env python3
# coding=utf-8
import logging

from waitress import serve
from config import Config
from openhopehack import create_app


def main():
    app = create_app(Config)

    config = Config()

    app_host = config.BIND_ADDRESS
    app_port = config.PORT
    logging.root.setLevel(config.LOG_LEVEL)

    # Start flask app using the built-in webserver if the LOG_LEVEL=DEBUG,
    # otherwise use waitress
    if logging.root.level == getattr(logging, "DEBUG"):
        app.run(debug=True, host=app_host, port=app_port)
    else:
        serve(app, host=app_host, port=app_port)


if __name__ == "__main__":
    main()
