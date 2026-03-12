# Lab 5 Loop

from datetime import datetime, time
from time import sleep


def dateDIFFInSeconds(date1, date2):
    timedelta = date2 - date1
    return timedelta.days * 24 * 3600 + timedelta.seconds


def daysHoursMinutesSecondsFromSeconds(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    return (days, hours, minutes, seconds)


leaving_date = datetime.strptime('2012-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')
now = datetime.now()


print("%dd days, %dh hours, %dm minutes, %ds seconds" % daysHoursMinutesSecondsFromSeconds(
    dateDIFFInSeconds(now, leaving_date)))
sleep(1)
now = datetime.now()
print("done")

