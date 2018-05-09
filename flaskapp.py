from flask import Flask, jsonify
import logging
application = Flask(__name__)

_logger = logging.getLogger('mainLogger')
lfhdlr = logging.FileHandler('/var/log/gumgum/flask_blog_app.log')
_logger.addHandler(lfhdlr)
_logger.setLevel(logging.INFO)

@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello World</h1>"

@application.route("/health")
def health():
    return jsonify({'status': 'ok'})

if __name__ == "__main__":
    _logger.info('Starting application.')
    application.run(host='0.0.0.0')
