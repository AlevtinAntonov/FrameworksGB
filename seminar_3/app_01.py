# Создать базу данных для хранения информации о студентах университета. База данных должна содержать две
# таблицы: "Студенты" и "Факультеты". В таблице "Студенты" должны быть следующие поля:
# id, имя, фамилия, возраст, пол, группа и id факультета. В таблице "Факультеты" должны быть следующие
# поля: id и название факультета. Необходимо создать связь между таблицами "Студенты" и "Факультеты".
# Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их факультета

from flask import Flask, render_template, jsonify

from seminar_3.model_01 import Student
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)


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

@app.cli.command("fill-db")
def fill_tables():
    count = 5
    # Добавляем пользователей
    for user in range(1, count + 1):
        new_user = Student(name=f'Name{user}', surname=f'SurName{user}', age=20, gender='male', group=10, faculty=1)
        db.session.add(new_user)
    db.session.commit()
    # Добавляем статьи
    for post in range(1, count ** 2):
        author = User.query.filter_by(username=f'user{post % count + 1}').first()
        new_post = Post(title=f'Post title {post}', content=f'Post content {post}', author=author)
        db.session.add(new_post)
    db.session.commit()

@app.route('/students/')
def get_all():
    students = Student.query.all()
    context = {'students': students}
    return render_template('students.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
