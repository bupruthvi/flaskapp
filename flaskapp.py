from flask import Flask, jsonify
from logging import FileHandler, WARNING
application = Flask(__name__)

file_handler = FileHandler('errorlog.txt')
file_handler.setlevel(WARNING)
app.logging.addHandler(file_handler)

@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello World</h1>"

@application.route("/health")
def health():
    return jsonify({'status': 'ok'})

if __name__ == "__main__":
    application.run(host='0.0.0.0')
