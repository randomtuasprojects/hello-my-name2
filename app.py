from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello():

    return "Hello, my name is Antti S!"

if __name__ == "__main__":

    app.run()