# Создать страницу, на которой будет форма для ввода двух чисел и выбор операции (сложение, вычитание, умножение или деление) и кнопка "Вычислить"
# При нажатии на кнопку будет произведено вычисление результата выбранной операции и переход на страницу с результатом.
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/calculate/', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        first = float(request.form.get('firstnum'))
        second = float(request.form.get('secondnum'))
        operation = request.form.get('operation')
        res = 0
        match operation:
            case "+":
                res = first + second
            case "-":
                res = first - second
            case "/":
                res = first / second
            case "*":
                res = first * second
        return f"{first} {operation} {second} = {res}"
    return render_template('calculate.html')


if __name__ == '__main__':
    app.run(debug=True)

# <select name="opt">
#         <option value="prefered" disabled selected>Выберите операцию:</option>
#         <option value="plus">+</option>
#         <option value="minus">-</option>
#         <option value="prod">*</option>
#         <option value="div">/</option>
#     </select>
#
# num1 = int(request.form.get('num1'))
#         num2 = int(request.form.get('num2'))
#         opt = request.form.get('opt')
#         match opt:
#             case 'plus':
#                 res = num1 + num2
#             case 'minus':
#                 res = num1 - num2
#             case 'prod':
#                 res = num1 * num2
#             case 'div':
#                 res = num1 / num2

