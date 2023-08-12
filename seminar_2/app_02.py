Создать страницу, на которой будет изображение и ссылка на другую страницу, на которой будет отображаться форма для загрузки изображений.

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Форма для загрузки файла</title>
</head>
<body>
<h1>Загружаем новый файл на сервер</h1>
<form method=post enctype=multipart/form-data>
    <input type=file name=file>
    <input type=submit value=Загрузить>
</form>
</body>
</html>


<a href="{{ url_for('form_page') }}">
    <img src="https://proprikol.ru/wp-content/uploads/2019/08/kartinki-nyashnye-kotiki-16.jpg" alt="котик)"
         title="12345" width="200" height="200">
</a>

<form method=post enctype=multipart/form-data>
    <input type=file name=file>
    <input type=submit value=Загрузить>
</form>

@app.route('/form/')
def form_page():
    return render_template('form_page.html')