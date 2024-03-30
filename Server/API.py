from Server.src.Messenge import Messange, Storer
from Server.src.User import User
from flask import Flask, request

get = ["GET"]
post = ["POST"]
p_g = ["POST", "GET"]

app = Flask(__name__)


@app.route("/regestration/qedsfw342refd/", methods=post)
def reg():
    if request.method == "POST":
        data = request.json
        user = User(data["login"], data["password"])
        if not user.have_user():
            return user.reg_user(name=data["name"])[0]
        else:
            return "HavingUser"


@app.route("/vhod/dsadi3dijap213d", methods=post)
def chek_reg():
    if request.method == "POST":
        data = request.json
        user = User(data["login"], data["password"])
        reged = user.chek_reg()
        if reged[1]:
            return reged[0]
        else:
            return reged[0]


@app.route("/get/messenge/<path:id>", methods=post)
def mesage(id):
    if request.method == "POST":
        s = Storer(id)
        data = request.json
        if data["type"] == "post":
            user = User(data["login"], data["password"])
            if user.chek_reg()[1]:
                m = Messange(data["content"], user.usr["parm"]
                             ["name"], data["login"])
                s.set_mes(m)
                if s.is_id():
                    if user.get_rules()["rules"]["WRITE"]:
                        s.write()
                        return "Succses"
                    else:
                        return "CanNotWrite"
                else:
                    if user.get_rules()["rules"]["CREATE"] and user.get_rules()["rules"]["CREATE_NOW"] < user.get_rules()["rules"]["CREATE_MAX"]:
                        user.create_room()
                        s.write()
                        return "Succses"
                    else:
                        return "CanNotCreate"
            else:
                return "NoThisUser"
        elif data["type"] == "get":
            data = request.json
            user = User(data["login"], data["password"])
            if user.chek_reg()[1]:
                if user.get_rules()["rules"]["READ"]:
                    if s.is_id():
                        return s.read()
                    else:
                        return "NoThisRoom"
                else:
                    return "CanNotRead"
            else:
                return "NoThisUser"


@app.route("/changes/users/who/", methods=post)
def changes():
    if request.method == "POST":
        data = request.json
        user = User(data["login"], data["password"])
        if user.chek_reg()[1]:
            return user.change_(data["rule"], data["znach"])
        else:
            return "NoThisUser"


@app.route("/get_usr_name/shaudipfl/fds", methods=post)
def get_user_name():
    if request.method == "POST":
        data = request.json
        user = User(data["login"], data["password"])
        if user.chek_reg()[1]:
            return user.usr["parm"]["name"]
        else:
            return "NoThisUser"
