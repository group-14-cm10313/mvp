import sqlite3
import json

def addToDB(json_obj):
    # Open a connection to an SQLite database
    conn = sqlite3.connect('sleep_data.db')
    c = conn.cursor()

    # Define the table schema
    table_schema = '''
    CREATE TABLE IF NOT EXISTS sleep_data (
        caffeine INTEGER,
        caffeine_sources TEXT,
        caffeine_times TEXT,
        sleepTime TEXT,
        wakeTime TEXT,
        toSleep TEXT,
        sleepQuality INTEGER,
        user TEXT
    )
    '''

    # Execute the table schema
    c.execute(table_schema)

    # Extract caffeine sources and times
    caffeine_sources = []
    caffeine_times = []
    for key, value in json_obj.items():
        if key.startswith('caffeine-source-'):
            index = int(key.split('-')[-1])
            caffeine_sources.insert(index, value)
        elif key.startswith('caffiene-time-'):
            index = int(key.split('-')[-1])
            caffeine_times.insert(index, value)

    # Insert the data into the table
    caffeine = int(json_obj['caffeine'])
    sleepTime = json_obj['sleepTime']
    wakeTime = json_obj['wakeTime']
    toSleep = json_obj['toSleep']
    sleepQuality = int(json_obj['sleepQuality'])
    user = json_obj['user']

    caffeine_sources_str = json.dumps(caffeine_sources)
    caffeine_times_str = json.dumps(caffeine_times)

    insert_data = f"INSERT INTO sleep_data VALUES ({caffeine}, '{caffeine_sources_str}', '{caffeine_times_str}', '{sleepTime}', '{wakeTime}', '{toSleep}', {sleepQuality}, '{user}')"
    c.execute(insert_data)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()