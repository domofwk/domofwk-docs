from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<h1>Bonjour, vous utilisez %s comme browser</h1>' % user_agent

if __name__ == '__main__':
    app.run(debug=True)

