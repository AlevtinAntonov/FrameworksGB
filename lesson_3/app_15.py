from flask import Flask, request, render_template
from flask_wtf import FlaskForm, CSRFProtect

from form_3 import RegistrationForm
from forms_1 import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = b'a3fc80778b3d2d998e5137808607c0cbcd8c924c21d9649f62ad8ab1414cec0f'
csrf = CSRFProtect(app)


# >>> import secrets
# >>> secrets.token_hex()

@app.route('/')
def index():
    return 'Hi!'


@app.route('/data/')
def data():
    return 'Your data!'


@app.route('/form', methods=['GET', 'POST'])
@csrf.exempt
def my_form():
    return 'No CSRF protection!'


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        pass
    return render_template('login.html', form=form)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
    # Обработка данных из формы
        email = form.email.data
        password = form.password.data
        print(email, password)
    ...
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
