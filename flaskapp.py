from flask import Flask, jsonify
import logging
application = Flask(__name__)

logger = logging.getLogger('mainLogger')
logger.addHandler(logging.FileHandler('/var/log/gumgum/flask_blog_app.log'))
logger.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
logger.setLevel(logging.WARNING)

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
