#!/usr/bin/env python3
# coding=utf-8
import logging
import os

from dotenv import load_dotenv
from waitress import serve

from openhopehack import create_app


def main():
    load_dotenv()

    app = create_app()

    app_host = os.getenv("BIND_ADDRESS")
    app_port = os.getenv("PORT")
    logging.root.setLevel(os.getenv("LOG_LEVEL", "INFO"))

    # Start flask app using the built-in webserver if the LOG_LEVEL=DEBUG,
    # otherwise use waitress
    if logging.root.level == getattr(logging, "DEBUG"):
        app.run(debug=True, host=app_host, port=app_port)
    else:
        serve(app, host=app_host, port=app_port)


if __name__ == "__main__":
    main()
