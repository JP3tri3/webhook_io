from json import dumps
import config, utilities, strategy, pprint, requests # type: ignore
from sanic import Sanic # type: ignore
from sanic.response import json # type: ignore
import messaging

app = Sanic(__name__)

db_symbol_object_format = config.DB_STORAGE_FORMAT
trigger_keys = db_symbol_object_format.keys()

def handle_symbol_db(args):
    if (args):
        print(f'\nupdating database:')
        all_objects = utilities.view_all_symbol_objects()
        pprint.pprint(all_objects)
        

        for symbol in utilities.view_all_symbol_objects():
            utilities.clear_db_object(symbol)

        for symbol in config.SYMBOLS:
            print(f'adding symbol: {symbol}')
            utilities.add_db_symbol_k_v(symbol, db_symbol_object_format)

handle_symbol_db(config.UPDATE_DB)

@app.route('/webhook', methods=['POST'])
async def webhook(request):
    try:
        data = request.json
        
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

                for key in trigger_keys:
                    if key in data:
                        print(key)
                        trigger_value = data[key]
                        utilities.update_db_object_value(symbol, key, trigger_value)

                print(f'\nchecking object:')
                triggers_object = utilities.view_data_object(symbol)
                pprint.pprint(triggers_object)
                strat_output = strategy.determine_trigger(triggers_object)
                print(f'state change: {strat_output}')

                if (strat_output != "none"):
                    symbol_info = config.SYMBOLS[symbol]
                    if (strat_output == 'open_long'):
                        exchange_payload = symbol_info['open_long']
                    
                    elif (strat_output == 'open_short'):
                        exchange_payload = symbol_info['open_short']

                    elif (strat_output == 'close_long'):
                        exchange_payload = symbol_info['close_long']

                    elif (strat_output == 'close_short'):
                        exchange_payload = symbol_info['close_short']
                        
                    print(f'\nsending payload to exchange')

                    strat_output = 'none' if (strat_output == 'close_long') or (strat_output == 'close_short') \
                        else strat_output

                    utilities.update_db_object_value(symbol, 'current_state', strat_output)

                    r = requests.post(config.OUTGOING_WEBHOOK_URL, data=dumps(exchange_payload), headers={'Content-Type': 'application/json'})

                    notification = messaging.handle_discord_messages(symbol, strat_output)
                    print(f'sending notification: {notification}')

                    r = requests.post(config.OUTGOING_WEBHOOK_URL_MESSAGING, data=dumps(notification), headers={'Content-Type': 'application/json'})

                return json({
                    "code": "success",
                    "message": "payload processed"
                })

            else:
                print("ERROR: process failed")
                return json({
                    "code": "error",
                    "message": "process failed"
                })

    except Exception as e:
        print("an exception occured - {}".format(e))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)