from runlog.run import Run
import sys, sqlite3
from datetime import datetime
conn = sqlite3.connect('runs.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS runs (
    id integer PRIMARY KEY,
    date integer NOT NULL,
    distance real NOT NULL,
    duration text NOT NULL,
    type text,
    notes text );""")

def main():
    print('\n=== runlog ===\n')
    c.execute("SELECT * FROM runs WHERE ID = (SELECT MAX(ID)  FROM runs);")
    row = c.fetchall()
    print(row)
    print('\n')
    print("1) Add a run\n")
    choice = input('What would you like to do? ')
    
    if choice == '1':
        add_run()
        
    conn.close()

def add_run():
    run_distance = input('Distance (miles): ')
    print('\n')
    run_time = input('Duration (hour:min:sec): ')
    print('\n')
    run_type = input('Type of run: ')
    print('\n')
    run_notes = input('Notes: ')

    c.execute("INSERT INTO runs (date, distance, duration, type, notes) VALUES (strftime('%s', 'now'), ?, ?, ?, ?)"
                    , (run_distance, run_time, run_type, run_notes))
    conn.commit()

if __name__ == '__main__':
    main()