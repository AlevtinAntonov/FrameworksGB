# Задание №3.
# Доработаем задачу про студентов.
# Создать базу данных для хранения информации о студентах и их оценках в учебном заведении.
# База данных должна содержать две таблицы: "Студенты" и "Оценки".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа и email.
# В таблице "Оценки" должны быть следующие поля: id, id студента, название предмета и оценка.
# Необходимо создать связь между таблицами "Студенты" и "Оценки".
# Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их оценок.
from random import choice

from flask import Flask, render_template, jsonify

from homework_3.model_students import GenderEnum, Faculty
from seminar_3.model_01 import Student
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../instance/student.db'
db = SQLAlchemy(app)
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


@app.cli.command("fill-students")
def fill_tables():
    count = 5
    # Добавляем факультеты
    for faculty in range(1, count + 1):
        new_faculty = Faculty(title=f'faculty{faculty}')
        db.session.add(new_faculty)
    db.session.commit()
    # Добавляем студентов
    for student in range(1, count ** 2):
        faculty = choice(range(1, 6))
        new_student = Student(name=f'Student{student}', surname=f'surname{student}', age=choice(range(18, 100)),
                              gender=choice([GenderEnum.MALE, GenderEnum.FEMALE]), group=choice(range(10, 15)),
                              faculty=faculty)
        db.session.add(new_student)
    db.session.commit()


@app.route('/students/')
def get_all():
    students = Student.query.all()
    context = {'students': students}
    return render_template('students.html', **context)


@app.route('/estimates/')
def get_all_est():
    students = Student.query.all()
    return render_template('estimates.html', students=students)


if __name__ == '__main__':
    app.run(debug=True)
