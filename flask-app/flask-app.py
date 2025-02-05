from flask import Flask

application = Flask(__name__)

@application.route("/")

def index():
    return "Hello World by Flask"

@application.route("/help")
def help():
    return "This ia a help page!"

if __name__== "__main__":
    application.run()