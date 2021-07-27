This application works to resolve issues with 3rd party exchanges that allow single webhook input triggers.  This application can be configured to receive multiple webhooks, check for the configured variables to match, then output a single trigger via webhook.  Currently implemented with a 3 trigger strategy example, can be expanded by updating strategy.py and db.json.

# Steps:
- pip install packages located in requirements.txt
- set config.WEBHOOK_PASSPHRASE to the passphrase included in JSON payload.
- set config.OUTGOING_WEBHOOK_URL to the output url (this will be provided by the exchange that you're trying to send the signal to)
- set exchange payload conditions (config.open_long, config.open_short, config.close_long, config.close_short)... this may be able to be optimized upon reviewing exchange payload examples
- setup webhook output in TV
- incoming JSON payload example (coming from TradingView or similiar application):

{
    "passphrase": "temp_passphrase",
    "symbol": "ETH",
	"tf": 2m,
	"value": 0
}

# payload explanation:
- "passphrase" is used to confirm TV wehbook is coming from your account
- "symbol" allows for configuring strat to be used with multiple symbols (configured in db.json)
- strategy is currently configured for 3 trigger inputs ("trigger_1", "trigger_2", "trigger_3"), utilizing "trigger_1" as the lowest timeframe
- "input":
0 = red/down/off
1 = green/up/on
-1 = no input to compare

# how to run:
- navigate to directory in terminal
- use command 'python app.py' to run application