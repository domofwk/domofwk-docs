from flask import Flask, render_template

app = Flask(__name__)

@app.route('/user/<nom>')
def index(nom):
    return render_template('index.html', name=nom)

if __name__ == '__main__':
    app.run(debug=True)


