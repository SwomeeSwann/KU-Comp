import datetime
import time

def date_to_unix(date):

    # assigned regular string date
    date_list = []
    date_list = date_list.split('-')
    
    year = date_list[0]
    month = date_list[1]
    day = date_list[2]

    date_time = datetime.datetime(year, month, day, 0, 0, 0)
    return (time.mktime(date_time.timetuple()))