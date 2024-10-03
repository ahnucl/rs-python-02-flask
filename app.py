from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!@#'


@app.route('/about')
def about():
    return 'Página sobre'


if __name__ == '__main__': # Execução manual
    app.run(debug=True) # Apenas para desenvolvimento