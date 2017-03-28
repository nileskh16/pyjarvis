import socket, httplib
from pytz import timezone
from datetime import datetime

def get_time():
  ini = timezone('Asia/Kolkata')
  cur_time = datetime.now(ini)
  return cur_time.strftime('%I hours %M minutes %S seconds %p %A %d %B %Y')

def is_internet():
    conn = httplib.HTTPConnection("www.google.com")
    try:
        conn.request("HEAD", "/")
        return True
    except Exception, err:
        return False

def machine_info():
    return socket.gethostname()
