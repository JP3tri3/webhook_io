import json
import pprint
import config, utilities, strategy
import requests # type: ignore
from flask import Flask, request, render_template # type: ignore

app = Flask(__name__)

# set to True to reset db.json
refresh_data = False

if refresh_data:
    print(f'\nrefreshing json:')
    utilities.refresh_data()

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
            strat_output = strategy.determine_trigger(triggers_object)
            print(f'strat_output: {strat_output}')
            if (strat_output != "none"):
                
                if (strat_output == 'open_long'):
                    exchange_payload = config.open_long
                
                elif (strat_output == 'open_short'):
                    exchange_payload = config.open_short

                elif (strat_output == 'close_long'):
                    exchange_payload = config.close_long

                elif (strat_output == 'close_short'):
                    exchange_payload = config.close_short
                print(f'\nsending payload to exchange')

                strat_output = 'none' if (strat_output == 'close_long') or (strat_output == 'close_short') \
                    else strat_output

                utilities.update_data(symbol, 'current_state', strat_output)
                r = requests.post(config.OUTGOING_WEBHOOK_URL, data=json.dumps(exchange_payload), headers={'Content-Type': 'application/json'})
            
            return {
                "code": "success",
                "message": "payload processed"
            }

        else:
            print("ERROR: process failed")
            return {
                "code": "error",
                "message": "process failed"
            }
