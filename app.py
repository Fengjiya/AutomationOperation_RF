from flask import Flask

import logging as logger

app = Flask(__name__)


@app.route('/')
def hello_world():
    logger.info("我是实验的API")
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
