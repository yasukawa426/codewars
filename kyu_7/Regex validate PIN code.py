def validate_pin(pin):
    if not pin.isdigit():
        return False
    
    
    if len(pin) == 4 or len(pin) == 6:
        return True
    
    return False