# Задание №4.
# Создайте форму регистрации пользователя с использованием Flask-WTF. Форма должна содержать следующие поля:
# ○ Имя пользователя (обязательное поле)
# ○ Электронная почта (обязательное поле, с валидацией на корректность ввода email)
# ○ Пароль (обязательное поле, с валидацией на минимальную длину пароля)
# ○ Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)
# После отправки формы данные должны сохраняться в базе данных (можно использовать SQLite)
# и выводиться сообщение об успешной регистрации. Если какое-то из обязательных полей не
# заполнено или данные не прошли валидацию, то должно выводиться соответствующее
# сообщение об ошибке.
# Дополнительно: добавьте проверку на уникальность имени пользователя и электронной почты в
# базе данных. Если такой пользователь уже зарегистрирован, то должно выводиться сообщение
# об ошибке.

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import CSRFProtect

from homework_3.form_reg_user import RegistrationForm
from lesson_3.model_03 import db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = b'a3fc80778b3d2d998e5137808607c0cbcd8c924c21d9649f62ad8ab1414cec0f'
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../instance/my_database.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hi!'


@app.route('/data/')
def data():
    return 'Your data!'


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.route('/registration/', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data.lower()
        email = form.email.data
        user = User(username=username, email=email)
        if User.query.filter(User.username == username).first() or User.query.filter(User.email == email).first():
            flash(f'Пользователь с username {username} или e-mail {email} уже существует')
            return redirect(url_for('registration'))
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Вы успешно зарегистрировались!')
        return redirect(url_for('registration'))
    return render_template('registration.html', form=form)


if __name__ == '__main__':
    app.run()
