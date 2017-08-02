#
# Script for utility/helper functions        
#
import datetime

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

# test function
if __name__ == '__main__':
    flog('hiiii')
    read_logs()
    #datetim()
