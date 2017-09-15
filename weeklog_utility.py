import datetime

def get_current_time() -> datetime.datetime:
    '''
    Returns the current time as datetime.datetime object
    '''
    return datetime.datetime.now()

def get_week(_dt: datetime.datetime) -> int:
    '''
    Returns the week number of the day provided
    '''
    return _dt.isocalendar()[1]

def get_current_week() -> int:
    '''
    Returns the week number of the current day
    '''
    return get_week(datetime.datetime.now())

def get_year(_dt: datetime.datetime) -> int:
    '''
    Returns the year number for the ISO week provided
    '''
    return _dt.isocalendar()[0]

def get_current_year() -> int:
    '''
    Returns the year number for the current ISO week
    '''
    return get_year(datetime.datetime.now())

def fb_time_to_datetime(fb_time: str) -> datetime.datetime:
    '''
    Parses the string of FogBugz dt column format and creates datetime object
    Returns the newly created datetime object
    '''
    year = int(fb_time[0:4])
    month = int(fb_time[5:7])
    day = int(fb_time[8:10])
    hour = int(fb_time[11:13])
    minute = int(fb_time[14:16])
    second = int(fb_time[17:19])
    return datetime.datetime(year, month, day, hour, minute, second)
