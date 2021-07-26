import json
import pprint
import config
import requests # type: ignore
from flask import Flask, request, render_template # type: ignore

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    
    data = json.loads(request.data)
    
    if data['passphrase'] != config.WEBHOOK_PASSPHRASE:
        return {
            "code": "error",
            "message": "Invalid Passphrase"
        }
    else:

            if data:
                print(pprint.pprint(data))
                r = requests.post(config.OUTGOING_WEBHOOK_URL, data=json.dumps(data), headers={'Content-Type': 'application/json'})
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
