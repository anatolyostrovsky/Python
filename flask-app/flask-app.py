from flask import Flask

application = Flask(__name__)

@application.route("/")

def index():
    return "Hello World by Flask"

if __name__== "__main__":
    application.run()