from flask import Flask, jsonify
import logging


application = Flask(__name__)

handler = logging.handlers.TimedRotatingFileHandler(
  '/var/log/gumgum/flask_blog_app.log', when='m', interval=1)
formatter = logging.Formatter(logging.BASIC_FORMAT)
handler.setFormatter(formatter)

logger = logging.getLogger('mainLogger')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

@application.route("/")
def hello():
    logger.debug('Instantiating definition.')
    return "<h1 style='color:blue'>Hello World</h1>"

@application.route("/health")
def health():
    return jsonify({'status': 'ok'})

if __name__ == "__main__":
    logger.info('Starting application.')
    application.run(host='0.0.0.0')
