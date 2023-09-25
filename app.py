from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)

app.static_folder = 'static'
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    if 'username' in session:
        return(render_template('home.html',uname = session['username']))
    return render_template('home.html')

def create_users_table():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)
    conn.commit()

# Call the function to create the users table
create_users_table()

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Query the database for the user
    cursor.execute("SELECT * FROM users WHERE email=?", (email,))
    user = cursor.fetchone()
    if user and user[3] == password:
        session['email'] = email
        session['username'] = user[1]
        return redirect('/')  # Redirect to the dashboard or a success page
    else:
        error_message = "Invalid email or password."
        return render_template('account.html', error_message=error_message)

# Signup route
@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['Username']
    email = request.form['Email']
    password = request.form['Password']

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Check if the email already exists in the database
    cursor.execute("SELECT * FROM users WHERE email=?", (email,))
    existing_user = cursor.fetchone()
    if existing_user:
        return (render_template('account.html',msg="User Exists"))

    # Insert the new user into the database
    cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
    conn.commit()

    session['email'] = email
    return redirect('/')  # Redirect to the dashboard or a success page

# Logout route
@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')

@app.route('/challenges')
def challenges():
    return render_template('challenges.html')

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/cases')
def cases():
    return render_template('cases.html')

@app.route('/easy')
def easy():
    return render_template('easy.html')

@app.route('/easylev2')
def easylev2():
    return render_template('easylev2.html')

@app.route('/easylev3')
def easylev3():
    return render_template('easylev3.html')

@app.route('/easylev4')
def easylev4():
    return render_template('easylev4.html')

@app.route('/easylev5')
def easylev5():
    return render_template('easylev5.html')

@app.route('/hard')
def hard():
    return render_template('hard.html')

@app.route('/hardlev2')
def hardlev2():
    return render_template('hardlev2.html')

@app.route('/hardlev3')
def hardlev3():
    return render_template('hardlev3.html')

@app.route('/hardlev4')
def hardlev4():
    return render_template('hardlev4.html')

@app.route('/hardlev5')
def hardlev5():
    return render_template('hardlev5.html')

@app.route('/medium')
def medium():
    return render_template('medium.html')

@app.route('/medlev2')
def medlev2():
    return render_template('medlev2.html')

@app.route('/medlev3')
def medlev3():
    return render_template('medlev3.html')

@app.route('/medlev4')
def medlev4():
    return render_template('medlev4.html')

@app.route('/medlev5')
def medlev5():
    return render_template('medlev5.html')

@app.route('/mix')
def mix():
    return render_template('mix.html')

@app.route('/punctuations')
def punctuations():
    return render_template('punctuations.html')

@app.route('/numbers')
def numbers():
    return render_template('numbers.html')

@app.route('/tutorial')
def tutorial():
    return render_template('tutorial.html')

if __name__ == '__main__':
    app.run(debug=True)