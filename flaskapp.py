from flask import Flask, jsonify
import logging
application = Flask(__name__)

logging.basicConfig(
  format='%(asctime)s %(levelname)s %(message)s',
  level=logging.WARNING,
  filename='/var/log/gumgum/flask_blog_app.log')

logger = logging.getLogger('mainLogger')

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
