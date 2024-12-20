from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_geek():
    return '<h1>Hello from my Raspberry pi</h1>'


if __name__ == "__main__":
    app.run(debug=True)
