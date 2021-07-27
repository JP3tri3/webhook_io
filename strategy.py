
def determine_trigger(data):
    current_state = data['current_state']
    trigger_1 = data['trigger_1']
    trigger_2 = data['trigger_2']
    trigger_3 = data['trigger_3']

    open_triggers_total = trigger_1 + trigger_2 + trigger_3
    close_triggers_total = trigger_2 + trigger_3

    trigger_status = ''

    if (current_state == 'none'):
        if (open_triggers_total == 3):
            trigger_status = 'open_long'
        elif (open_triggers_total == 0):
            trigger_status = 'open_short'
        else:
            trigger_status = 'none'

    elif (current_state == 'open_long'):
        trigger_status = 'close_long' if (close_triggers_total == 0) or (close_triggers_total == 1) \
            else 'none'

    elif (current_state == 'open_short'):
        trigger_status = 'close_short' if (close_triggers_total >= 1) \
            else 'none'

    else:
        trigger_status = 'none'
    
    return trigger_status