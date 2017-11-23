import json
from sys import argv
from bottle import route,run,template, static_file,request

@route('/myndir/<nafn>')
def static(nafn):
    return static_file(nafn, root='/myndir')



@route("/")
def home():
    if request.get_cookie("visited"):
        hallo = request.get_cookie("visited")
        ioStream = open('myndir.json', 'r', encoding='utf-8')
        dData = json.load(ioStream)
        ioStream.close()
        return template("index2.tpl",a = "Cookie",gogn=dData)
    else:
        return template("index.tpl")


@route("/skra", method = 'POST')
def index():


    ioStream = open('myndir.json', 'r', encoding='utf-8')
    dData = json.load(ioStream)
    ioStream.close()
    return template("index2.tpl", gogn=dData)
run(host='localhost', port=8080, debug=True, Realoader=True)


