from html import escape

from flask import Flask, render_template, request, flash, redirect, url_for, session

app = Flask(__name__)
app.secret_key = b''


# >>> import secrets
# >>> secrets.token_hex()

@app.route('/')
def index():
    return 'Hi!'


@app.route('/index/')
def new_index():
    return render_template('index.html')


@app.route('/check_age/', methods=['GET', 'POST'])
def check_age():
    if request.method == 'POST':
        name = escape(request.form.get('name'))
        age = int(request.form.get('age'))
        if 100 > age >= 18:
            return f"Доступ разрешен -> пользователю {name}"
        return f"Доступ пользователю {name} запрещен!"
    return render_template('check_age.html')


@app.route('/square/', methods=['GET', 'POST'])
def square():
    if request.method == 'POST':
        number = float(request.form.get('number'))
        data = {"number": number, "square": number ** 2}
        return render_template('square.html', data=data)
    return render_template('square.html')


@app.route('/msg', methods=['GET', 'POST'])
def msg():
    if request.method == 'POST':
        name = escape(request.form.get('name'))
        flash(f'Привет, {name}!', 'success')
        return redirect(url_for('msg'))
    return render_template('flash-message.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username')
        return redirect(url_for('new_index'))
    return render_template('login.html')


@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('new_index'))


if __name__ == '__main__':
    app.run(debug=True)
