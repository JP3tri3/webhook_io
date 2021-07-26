import json
import pprint
import config, utilities, strategy

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
            print(f'\nincoming data:')
            print(pprint.pprint(data))

            symbol = data['symbol']
            trigger = data['trigger']
            trigger_value = data['value']
            triggers_object = utilities.update_data(symbol, trigger, trigger_value)

            print(f'\nchecking object:')
            print(pprint.pprint(triggers_object))


            r = requests.post(config.OUTGOING_WEBHOOK_URL, data=json.dumps(data), headers={'Content-Type': 'application/json'})
            
            return {
                "code": "success",
                "message": "payload processed"
            }

        else:
            print("order failed")
            return {
                "code": "error",
                "message": "process failed"
            }
