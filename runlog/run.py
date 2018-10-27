from datetime import timedelta
from datetime import datetime
import persistent

class Run(persistent.Persistent):

    def __init__(self, distance = None, time = None):
        self.distance = distance
        if time:
            t = datetime.strptime(time, "%H:%M:%S")
            self.time = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
            #self.pace = (time / 60.0) / distance



    

