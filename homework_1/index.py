from flask import Flask, render_template
from homework_1.db import _news, _about, _contacts, _clothes, _shoes, _jackets

app = Flask(__name__)


@app.route('/')
def index():
    context = {'title': 'Главная'}
    return render_template('index.html', **context)


@app.route('/task7/')
def task_7():
    context = {'lst_news': _news,
               'page_title': [' Задание 7', 'страница с блоками новостей'],
               'task_text': "Текст задания: Написать функцию, которая будет выводить на экран HTML страницу с блоками "
                            "новостей."
                            "Каждый блок должен содержать заголовок новости, краткое описание и дату "
                            "публикации.Данные о новостях должны быть переданы в шаблон через контекст.",
               }
    return render_template('task_7.html', **context)


@app.route('/task8/')
def task_8():
    context = {'page_title': [' Задание 8', 'создать страницы "О нас" и "Контакты"'],
               'task_text': 'Текст задания: Создать базовый шаблон для всего сайта, содержащий общие элементы дизайна '
                            '(шапка, меню, подвал), и дочерние шаблоны для каждой отдельной страницы. Например, '
                            'создать страницу "О нас" и "Контакты", используя базовый шаблон.',
               }
    return render_template('task_8.html', **context)


@app.route('/about/')
def task_8_about():
    context = {'title': 'О нас',
               'about_us': _about,
               }
    return render_template('task_8_about.html', **context)


@app.route('/contacts/')
def task_8_contacts():
    context = {'title': 'Контакты',
               'our_contacts': _contacts,
               }
    return render_template('task_8_contacts.html', **context)


@app.route('/task9/')
def task_9():
    context = {'page_title': [' Задание 9', 'Создать базовый шаблон для интернет-магазина'],
               'task_text': 'Текст задания: Создать базовый шаблон для интернет-магазина, содержащий общие элементы '
                            'дизайна (шапка, меню, подвал), и дочерние шаблоны для страниц категорий товаров и '
                            'отдельных товаров. Например, создать страницы "Одежда", "Обувь" и "Куртка", '
                            'используя базовый шаблон.',
               }
    return render_template('task_9.html', **context)


@app.route('/shop/')
def shop_main():
    context = {
        'shop_title': 'Магазин одежды',
        'start_image': '/static/image/fashion.jpg',
        'brand': '/static/image/brand.png'
    }
    return render_template('index_shop.html', **context)


@app.route('/clothes/')
def shop_clothes():
    context = {
        'page_title': 'Одежда',
        'lst_items': _clothes,
    }
    return render_template('page.html', **context)


@app.route('/shoes/')
def shop_shoes():
    context = {
        'page_title': 'Обувь',
        'lst_items': _shoes,
    }
    return render_template('page.html', **context)


@app.route('/jackets/')
def shop_jackets():
    context = {
        'page_title': 'Куртки',
        'lst_items': _jackets,
    }
    return render_template('page.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
