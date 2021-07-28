
def determine_trigger(data):
    current_state = data['current_state']
    low_tf_val = data['2m']
    mid_tf_val = data['16m']
    high_tf_val = data['96m']

    new_state = None

    if (current_state == 'none'):
        if (low_tf_val == 1) and (mid_tf_val == 1) and (high_tf_val == 1):
            new_state = 'open_long'
        elif (low_tf_val == 0) and (mid_tf_val == 0) and (high_tf_val == 0):
            new_state = 'open_short'
        else:
            new_state = 'none'

    elif (current_state == 'open_long'):
        if (mid_tf_val == 0) or (high_tf_val == 0):
            new_state = 'close_long' 
        else:
            new_state = 'none'

    elif (current_state == 'open_short'):
        if (mid_tf_val == 1) or (high_tf_val == 1):
            new_state = 'close_long'
        else:
            new_state = 'none'

    else:
        new_state = 'none'
    
    return new_state