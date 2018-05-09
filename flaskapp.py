from flask import Flask, jsonify
application = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello World</h1>"

@app.route("/health")
def health():
    return jsonify({'status': 'ok'})

if __name__ == "__main__":
    application.run(host='0.0.0.0')
