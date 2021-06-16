from flask import Flask, render_template, request, redirect, session
from logic.user_logic import UserLogic
import requests
import bcrypt

app = Flask(__name__)
app.secret_key = "soy_una_clave_secreta"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    data = {}
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        data["secret"] = "6Lcs1RobAAAAAPSZaOpIsjO0D0BwJq2YuFdefqm-"
        data["response"] = request.form["g-recaptcha-response"]
        response = requests.post(
            "https://www.google.com/recaptcha/api/siteverify", params=data
        )
        print(response)
        if response.status_code == 200:
            messageJson = response.json()
            print(messageJson)
            if messageJson["success"]:
                logic = UserLogic()
                userName = request.form["userName"]
                userEmail = request.form["userEmail"]
                passwd = request.form["passwd"]
                confpasswd = request.form["confpasswd"]
                if passwd == confpasswd:
                    salt = bcrypt.gensalt(rounds=14)
                    strSalt = salt.decode("utf-8")
                    encPasswd = passwd.encode("utf-8")
                    hashPasswd = bcrypt.hashpw(encPasswd, salt)
                    strPasswd = hashPasswd.decode("utf-8")
                    rows = logic.insertUser(userName, userEmail, strPasswd, strSalt)
                    return redirect("login")
                else:
                    return redirect("register")
            return redirect("register")
        return redirect("register")
                


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        logic = UserLogic()
        userName = request.form["userName"]
        passwd = request.form["passwd"]
        userDict = logic.getUserByName(userName)
        salt = userDict["salt"].encode("utf-8")
        hashPasswd = bcrypt.hashpw(passwd.encode("utf-8"), salt)
        dbPasswd = userDict["password"].encode("utf-8")
        if hashPasswd == dbPasswd:
            session["login_user"] = userName
            session["loggedIn"] = True
            return redirect("dashboard")
        else:
            return redirect("login")
    


@app.route("/dashboard")
def dashboard():
    if session.get("loggedIn"):
        user = session.get("login_user")
        return render_template("dashboard.html", user=user)
    else:
        return redirect("login")


if __name__ == "__main__":
    app.run(debug=True)
