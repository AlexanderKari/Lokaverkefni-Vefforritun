import json
from sys import argv
from bottle import route,run,template, static_file,request,redirect

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

    username = request.forms.get('notendanafn')
    password = request.forms.get('lykilord')

    with open("users.txt","r") as f:
        users = f.read()
        users = users.split(",")
        login = False
        for a in users:
            user = a.split(":")
            if username == user[0]:
                if password == user[1]:
                    nafn = username
                    pas = password
                    login = True
        if login == True:
            ioStream = open('myndir.json', 'r', encoding='utf-8')
            dData = json.load(ioStream)
            ioStream.close()
            return template("index2.tpl", gogn=dData,n = nafn,p = pas)
        else:
            redirect('http://localhost:8080/')
run(host='localhost', port=8080, debug=True, Realoader=True)


