# Создать страницу, на которой будет форма для ввода текста и кнопка "Отправить"
# При нажатии кнопки будет произведен подсчет количества слов в тексте и переход на страницу
# с результатом.
from html import escape

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/send_text/', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        text = escape(request.form.get('text'))
        return f"количество слов {len(text.split(' '))}"
    return render_template("text.html")

if __name__ == '__main__':
    app.run(debug=True)