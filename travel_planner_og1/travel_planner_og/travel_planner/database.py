import sqlite3

DB_NAME = "users.db"

def get_conn():
    conn = sqlite3.connect(DB_NAME, timeout=10, check_same_thread=False)
    return conn

def init_db():
    conn = get_conn()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS trips (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                city TEXT NOT NULL,
                start_date TEXT NOT NULL,
                end_date TEXT NOT NULL,
                days INTEGER NOT NULL,
                budget INTEGER NOT NULL,
                style TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT UNIQUE NOT NULL,
                min_budget INTEGER NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                city TEXT NOT NULL,
                visited_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        cities_data = [
            ('goa', 5000),
            ('delhi', 8000),
            ('mumbai', 10000),
            ('jaipur', 6000),
            ('ahmedabad', 7000),
            ('paris', 20000),
            ('dubai', 25000),
            ('london', 30000),
            ('newyork', 35000),
            ('singapore', 28000)
        ]
        for city, min_budget in cities_data:
            cursor.execute('INSERT OR IGNORE INTO cities (city, min_budget) VALUES (?, ?)', (city, min_budget))
        conn.commit()
    finally:
        conn.close()

def add_user(username, password):
    conn = get_conn()
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def get_user(username):
    conn = get_conn()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        return cursor.fetchone()
    finally:
        conn.close()

def save_trip(username, city, start_date, end_date, days, budget, style):
    conn = get_conn()
    try:
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO trips (username, city, start_date, end_date, days, budget, style) VALUES (?, ?, ?, ?, ?, ?, ?)',
            (username, city, start_date, end_date, days, budget, style)
        )
        conn.commit()
    finally:
        conn.close()

def get_user_trips(username):
    conn = get_conn()
    try:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT id, city, start_date, end_date, days, budget, style FROM trips WHERE username = ? ORDER BY start_date ASC',
            (username,)
        )
        return cursor.fetchall()
    finally:
        conn.close()

def get_min_budget(city):
    conn = get_conn()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT min_budget FROM cities WHERE city = ?', (city.lower(),))
        result = cursor.fetchone()
        return result[0] if result else None
    finally:
        conn.close()

def delete_trip(trip_id, username):
    conn = get_conn()
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM trips WHERE id = ? AND username = ?', (trip_id, username))
        conn.commit()
    finally:
        conn.close()

def save_history(username, city):
    conn = get_conn()
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO history (username, city) VALUES (?, ?)", (username, city))
        conn.commit()
    finally:
        conn.close()