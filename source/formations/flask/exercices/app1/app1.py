from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Bonjour le monde</h1>'

if __name__ == '__main__':
    app.run(debug=False)
