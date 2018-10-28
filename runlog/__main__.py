import sys, sqlite3, time, pandas as pd
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
    week_distance = 0
    print('\n=== runlog ===\n')

    for row in c.execute("SELECT * FROM runs WHERE date BETWEEN strftime('%s', 'now') - 604800 AND strftime('%s', 'now')"):
        week_distance += row[2]
    
    print('Past 7 days mileage: ', week_distance, '\n')
    
    print("1) Add a run\n")
    print("2) View recent runs\n")
    choice = input('What would you like to do? ')
    
    if choice == '1':
        add_run()
    elif choice == '2':
        view_runs()
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

def view_runs():
    n = input("How many runs would you like to view?: ")
    sql = "SELECT * FROM runs ORDER BY date DESC LIMIT %s;" % (n)
    print(pd.read_sql_query(sql, conn))

if __name__ == '__main__':
    main()