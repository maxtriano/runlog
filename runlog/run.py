from datetime import timedelta
from datetime import datetime
import ZODB, ZODB.FileStorage, BTrees.OOBTree, transaction, persistent

class Run(persistent.Persistent):

    def __init__(self, distance, time):
        self.date = datetime.now()
        self.distance = distance
        t = datetime.strptime(time, "%H:%M:%S")
        self.time = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
        self.pace = (time / 60.0) / distance

    storage=ZODB.FileStorage.FileStorage("runs.fs")
    db=ZODB.DB(storage)
    connection=db.open()
    root = connection.root()
    
    if not root.has_key("runs"):
        root.runs = BTrees.OOBTree.BTree()
    

    

