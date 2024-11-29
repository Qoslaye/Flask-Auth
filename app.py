from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__)
app.secret_key = '_5#y2L"F4Q8z'  # Required for flashing messages

@app.route('/')
def home():
    # Home page with a link to the authentication form
    return render_template('home.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        # Render Success.html when accessed via GET (after a successful login)
        return render_template('success.html')
    elif request.method == 'POST':
        password = request.form['password']
        if password == '123':
            flash('Login successful')
            # Redirect to /login to ensure the GET method renders success.html
            return redirect(url_for('login'))
        else:
            flash('Invalid password. Please try again.')
            return redirect(url_for('form'))

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
