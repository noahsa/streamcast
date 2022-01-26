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
def forecast(method):
    data = request.data or '{}'
    body = json.loads(data)
    if str(method) == 'arima':
        predictions = arima(body)
    elif str(method) == 'ets':
        predictions = ets(body)
    else:
        predictions = {'predictions': 'invalid method'}

    return jsonify(predictions)