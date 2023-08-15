from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi!'


@app.route('/data/')
def data():
    return 'Your data!'


if __name__ == '__main__':
    app.run(debug=True)
