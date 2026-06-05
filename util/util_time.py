from datetime import datetime

def getCurrentDateIime():
    now = datetime.now()
    return now.strftime('%Y: %m: %d: %H:%M:%S')