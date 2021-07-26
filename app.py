import json
import time
import config
from flask import Flask, request, jsonify, render_template # type: ignore

app = Flask(__name__)
myTime = int(time.time() * 1000)
trendFlag = False

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/webhook', methods=['POST'])
def webhook():
    # print(request.data)
    data = json.loads(request.data)
    trend = data["strategy"]["flag"]

    if data['passphrase'] != config.WEBHOOK_PASSPHRASE:
        return {
            "code": "error",
            "message": "Invalid Passphrase"
        }
    else:

        # print(data['ticker'])
        # print(data['bar'])

        if (trendFlag == False):
            return {
                "code": "downtrend, waiting"
            }
        else:
            side = data['strategy']['order_action'].upper()
            quantity = data['strategy']['order_contracts']
            ticker = data['ticker']
            test_data = 

            if order_response:
                return {
                    "code": "success",
                    "message": "order executed"
                }
            else:
                print("order failed")
                return {
                    "code": "error",
                    "message": "order failed"
                }
