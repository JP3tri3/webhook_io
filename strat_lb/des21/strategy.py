def determine_trigger(data):
    try:
        current_state = data['current_state']
        vwap6h_val = data['vwap6h']
        wave6h_val = data['wave6h']
        vwap3h_val = data['vwap3h']
        vwap25m_val = data['vwap25m']
        MVAlgo25m_val = data['MVAlgo25m']
        Supertrend25m_val = data['Supertrend25m']

        new_state = None

        if (current_state == 'none'):
            if (vwap6h_val > 0) and (wave6h_val > 0) and (vwap3h_val > 0) and (vwap25m_val > 0) and (MVAlgo25m_val == 1) and (Supertrend25m_val == 1):
                new_state = 'open_long'
            elif (vwap6h_val < 0) and (wave6h_val < 0) and (vwap3h_val < 0) and (vwap25m_val < 0) and (MVAlgo25m_val == 0) and (Supertrend25m_val == 0):
                new_state = 'open_short'
            else:
                new_state = 'none'

        elif (current_state == 'open_long'):
            if (MVAlgo25m_val == 0) or (Supertrend25m_val == 0) or (vwap25m_val < 0):
                new_state = 'close_long' 
            else:
                new_state = 'none'

        elif (current_state == 'open_short'):
            if (MVAlgo25m_val == 1) or (Supertrend25m_val == 1) or (vwap25m_val > 0):
                new_state = 'close_long'
            else:
                new_state = 'none'

        else:
            new_state = 'none'
        
        return new_state
    except Exception as e:
            print("an exception occured - {}".format(e))