This application works to resolve issues with 3rd party exchanges that allow single webhook input triggers.  This application can be configured to receive multiple webhooks, check for the configured variables to match, then output a single trigger via webhook.

Steps:
- pip install packages located in requirements.txt
- set config.WEBHOOK_PASSPHRASE to the passphrase included in JSON payload.
- set config.OUTGOING_WEBHOOK_URL to the output url (this will be provided by the exchange that you're trying to send the signal to)

(under development, UPDATE README)
- set trigger values in 
- incoming JSON payload example (coming from TradingView or similiar application):

{
    "passphrase": "temp_passphrase",
    "timeframe": "4m",
    "trigger_1": "test"
}

- use command 'flask run' to run application