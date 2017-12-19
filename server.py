from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

def make_app():
    app.debug = True
    app.port = 8080

    return app


if __name__ == '__main__':
    app = make_app()
    app.run()
