# Создать страницу, на которой будет форма для ввода логина и пароля
# При нажатии на кнопку "Отправить" будет произведена проверка соответствия логина и пароля и переход на страницу
# приветствия пользователя или страницу с ошибкой.
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/form/', methods=['GET', 'POST'])
def form_page():
    return render_template('index3.html')


if __name__ == '__main__':
    app.run(debug=True)

@app.route('/form/', methods=['GET', 'POST'])
def form_page():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        if name == "Ivan" and password == "pass":
            return redirect(url_for('hello_page', name=name))
        return render_template('form_page.html', error=True)
    return render_template('form_page.html', error=None)

{% if error %}
    <h2>Ошибка доступа! Неверный логин или пароль</h2>
{% endif %}
<form method=post enctype=multipart/form-data>
    <input type="text" placeholder="Введите имя" name="name"><br>
    <input type="password" placeholder="Введите пароль" name="password"><br><br>
    <input type=submit value=Загрузить>
</form>
