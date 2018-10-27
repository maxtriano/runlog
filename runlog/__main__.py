from .run import Run
import sys
from datetime import datetime
import ZODB, ZODB.FileStorage, BTrees.OOBTree, transaction, persistent

storage=ZODB.FileStorage.FileStorage("runs.fs")
db=ZODB.DB(storage)
connection=db.open()
root = connection.root()

if 'runs' not in root:   
    root['runs'] = BTrees.OOBTree.BTree()

runs = root['runs']

def add_run(distance, time):
    runs[datetime.now()] = Run(distance, time)
    root["runs"] = runs
    transaction.commit

def main():
    print('\n=== runlog ===\n\n')
    print("1) Add a run")


if __name__ == '__main__':
    main()