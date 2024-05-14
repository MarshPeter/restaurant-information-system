from flask import Flask

class Test:
    def test(self):
        print("Hello")


test = Test()

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World</p>"

@app.route("/test")
def hello():
    return "<p>This is a different page</p>"
