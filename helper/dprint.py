
from datetime import datetime as dt

def dprint(msg: str):
  date_str = "[" + dt.now().isoformat(sep = " ",timespec='seconds') + dt.ut+ "]"
  print(date_str,msg)

  