from flask import Flask

application = Flask(__name__)

@application.route("/")

def index():
    return "Hello World by Flask"

@application.route("/help")
def help():
    return "This ia a help page!"

@application.route("/user")
def user():
    return "This ia a user page!"

@application.route("/user/<username>")
def showuserpage(username):
    return "Hello " + username.upper()

@application.route("/path/<path:subpath>")
def print_subpath(subpath):
    return "Subpath is: " + subpath

@application.route("/square/<int:x>") 
def count_square(x):
    return "Your number Squared is: " + str(x * x)

@application.route("/travel")
def show_html_page():
    myfile = open("travel.html", mode = 'r')
    page = myfile.read()

    return page

if __name__== "__main__":
    application.run()