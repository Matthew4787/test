from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy database to store user data (username, password)
users_db = {}

@app.route('/')
def home():
    return redirect(url_for('login'))

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if the user exists in the "database"
        if username in users_db and users_db[username] == password:
            return f"Welcome, {username}!"
        else:
            flash('Invalid username or password!')
            return redirect(url_for('login'))
    return render_template('login.html')

# Route for the sign-up page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if username already exists
        if username in users_db:
            flash('Username already taken!')
            return redirect(url_for('signup'))

        # Save the new user to the "database"
        users_db[username] = password
        flash('Sign-up successful! Please login.')
        return redirect(url_for('login'))
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
