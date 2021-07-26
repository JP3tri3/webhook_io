import json
import time
import config
from flask import Flask, request, jsonify, render_template # type: ignore

app = Flask(__name__)
myTime = int(time.time() * 1000)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    print(request.data)
    data = json.loads(request.data)

    if data['passphrase'] != config.WEBHOOK_PASSPHRASE:
        return {
            "code": "error",
            "message": "Invalid Passphrase"
        }
    else:

            if data:
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
