from bottle import *



@route("/")
def home():
    return template("index.tpl")
run(host='localhost', port=8080, debug=True, Realoader=True)
