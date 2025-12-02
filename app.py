from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from werkzeug.security import generate_password_hash

app = Flask(__name__)

# MySQL Configuration for Gitpod
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="user_management"
    )

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup')
def signup_page():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def handle_signup():
    username = request.form['username']
    password = request.form['password']
    hashed = generate_password_hash(password)
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tbl_user (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(80) UNIQUE NOT NULL,
            password_hash VARCHAR(255) NOT NULL
        )
    ''')
    
    try:
        cursor.execute(
            'INSERT INTO tbl_user (username, password_hash) VALUES (%s, %s)',
            (username, hashed)
        )
        conn.commit()
        return "✅ User created successfully! <a href='/'>Go home</a>"
    except mysql.connector.IntegrityError:
        return "❌ Username already exists!"
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from werkzeug.security import generate_password_hash

app = Flask(__name__)

# MySQL Configuration for Gitpod
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="user_management"
    )

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup')
def signup_page():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def handle_signup():
    username = request.form['username']
    password = request.form['password']
    hashed = generate_password_hash(password)
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tbl_user (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(80) UNIQUE NOT NULL,
            password_hash VARCHAR(255) NOT NULL
        )
    ''')
    
    try:
        cursor.execute(
            'INSERT INTO tbl_user (username, password_hash) VALUES (%s, %s)',
            (username, hashed)
        )
        conn.commit()
        return "✅ User created successfully! <a href='/'>Go home</a>"
    except mysql.connector.IntegrityError:
        return "❌ Username already exists!"
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from werkzeug.security import generate_password_hash

app = Flask(__name__)

# MySQL Configuration for Gitpod
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="user_management"
    )

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup')
def signup_page():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def handle_signup():
    username = request.form['username']
    password = request.form['password']
    hashed = generate_password_hash(password)
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tbl_user (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(80) UNIQUE NOT NULL,
            password_hash VARCHAR(255) NOT NULL
        )
    ''')
    
    try:
        cursor.execute(
            'INSERT INTO tbl_user (username, password_hash) VALUES (%s, %s)',
            (username, hashed)
        )
        conn.commit()
        return "✅ User created successfully! <a href='/'>Go home</a>"
    except mysql.connector.IntegrityError:
        return "❌ Username already exists!"
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)