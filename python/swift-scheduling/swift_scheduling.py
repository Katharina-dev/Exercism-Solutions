from datetime import datetime, timedelta

def delivery_date(start, description):

    dt = datetime.strptime(start, "%Y-%m-%dT%H:%M:%S")
    m = dt.minute
    dt = dt.replace(minute=0)
    
    
    if description == "NOW":
        dt += timedelta(hours=2)
        dt = dt.replace(minute=m)
        
    elif description == "ASAP":
        if dt.hour < 13:
            dt = dt.replace(hour=17)   
        else:
            dt = dt.replace(hour=13)   
            dt += timedelta(days=1)
        
    elif description == "EOW":
        w = dt.weekday()
        if w < 3:
            delta = 4 - w
            dt = dt.replace(hour=17)
        else:
            delta = 6 - w
            dt = dt.replace(hour=20)
        dt += timedelta(days=delta)
        
    elif description[-1] == "M":
        number = int(description[:-1])
        if dt.month >= number:
            dt += timedelta(days=365)
        dt = dt.replace(month=number, day=1, hour=8)
        while dt.weekday() in (5, 6):
            dt += timedelta(days=1)
    
    elif description[0] == "Q":
        number = int(description[1:])
        if dt.month > 3 * number:
            dt += timedelta(days=365)
        dt = dt.replace(month=3*number, hour=8)
        if number in (1, 4):
            dt = dt.replace(day=31)
        elif number in (2, 3):
            dt = dt.replace(day=30)
        while dt.weekday() in (5, 6):
            dt -= timedelta(days=1)
            
    return dt.strftime("%Y-%m-%dT%H:%M:%S")
    
