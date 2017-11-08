
def point_to_microsec(position, time_interval):
    return position * time_interval

def datestring_to_microsec(date):
    hour = int(date[8:10])
    minute = int(date[10:12])
    second = int(date[12:14])
    millisec = int(date[14:])

    sec = hour * 60 * 60 + minute * 60 + second
    return sec * 1000000 + millisec * 1000

def add_instance_method(klass, method):
    setattr(klass, method.__name__, method)  
