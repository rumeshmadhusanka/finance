import requests
from flask import Flask, jsonify

from modules.config import Config as Conf

app = Flask(__name__)
app.config.from_object(Conf)


@app.route('/', methods=['GET'])
def index():
    return jsonify({"Hello": "World"})


@app.route('/ping/', methods=['GET'])
def ping():
    try:
        r = requests.get(Conf.API_GATEWAY_HEALTH_ENDPOINT)
        return jsonify(r.json())
    except ConnectionError as e:
        return "Error"


if __name__ == '__main__':
    app.run(port=app.config['PORT'], debug=True)
