import json

from flask import (
    Flask,
    jsonify,
    request
)

from forecast import (
    arima,
    ets
)

application = Flask(__name__)

@application.route('/')
@application.route('/status')
def status():
    return jsonify({'status': 'ok'})

@application.route('/forecast/<method>', methods=['POST'])
def forecast():
    data = request.data or '{}'
    body = json.loads(data)
    if method == 'arima':
        predictions = arima(body)
    elif method == 'ets':
        predictions = ets(body)
    else:
        predictions = {'predictions': 'invalid method'}

    return jsonify(predictions)