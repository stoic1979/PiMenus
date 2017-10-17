#
# Script for utility/helper functions
#
import datetime
import os

def flog(msg):
    """
    function to log msg in file and also print on console
    """
    f = open("logs.txt", "a")
    print msg
    now = datetime.datetime.now()
    f.write("%s %s\n" % (now, msg))
    f.close()


def read_logs():
    try:
        f = open('logs.txt', "r")
        lines = f.readlines()
        f.close()
        return lines
    except:
        return []


def datetim():
    now = datetime.datetime.now()
    print str(now)


def uptime():
    time = {}
    try:
        f = open( "/proc/uptime" )
        contents = f.read().split()

        f.close()
    except:
        return "Cannot open uptime file: /proc/uptime"

    total_seconds = float(contents[0])
    # Helper vars:
    MINUTE = 60
    HOUR = MINUTE * 60
    DAY = HOUR * 24

    # Get the days, hours, etc:
    days = int(total_seconds / DAY)

    hours = int((total_seconds % DAY) / HOUR)

    minutes = int((total_seconds % HOUR) / MINUTE)

    seconds = int(total_seconds % MINUTE)

    # Build up the pretty string (like this: "N days, N hours, N minutes, N seconds")
    string = ""

    if days < 99:
        string += "0" + str(days)
    else:
        string += str(days)

    string += ":"

    if hours < 10:
        string += "0" + str(hours)
    else:
        string += str(hours)

    string += ":"

    if minutes < 10:
        string += "0" + str(minutes)
    else:
        string += str(minutes)

    string += ":"

    if seconds < 10:
        string += "0" + str(seconds)
    else:
        string += str(seconds)

    return string


# test function
if __name__ == '__main__':
    flog('hiiii')
    read_logs()
    datetim()
    uptime()
