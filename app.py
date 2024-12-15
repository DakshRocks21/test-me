from flask import Flask, request
import sqlite3

app = Flask(__name__)

# Set up the database (for demonstration purposes)
def init_db():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )
    ''')
    cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")
    conn.commit()
    conn.close()

@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Intentionally vulnerable query (DO NOT use in production)
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()

    if user:
        return f"Welcome, {user[1]}!"
    else:
        return "Invalid username or password."

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
