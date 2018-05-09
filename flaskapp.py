from flask import Flask, jsonify
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello World</h1>"

@application.route("/health")
def health():
    return jsonify({'status': 'ok'})

if __name__ == "__main__":
    application.run(host='0.0.0.0')
