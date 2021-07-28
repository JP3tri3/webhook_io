

def handle_discord_messages(symbol, state):
    content = (f'{symbol} - new trade status: {state}')
    return {"content" : content}

