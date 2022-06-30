
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/admin")
def hello_admin():
    return f"<h1> Hello admin </h1>"
@app.route("/user/<name>") #chuyền biến name
def hello_user(name):
    if name == "admin":
        #chuyển trang
        return redirect(url_for("hello_admin"))
    return f"<h1> Hello {name} </h1>"

@app.route("/blog/<int:id>") #Truyền ID
def blog(id):
    return f"<h1> Hello {id} </h1>"

@app.route("/")
def hello():
    #return render_template("index.html", content = "flask", cars =["Vìn", "Honda", "Mec"])
    return render_template("home.html")
@app.route("/login", methods = ["POST","GET"])
def login():
    if request.method == "POST":
        user_name = request.form["name"]
        if user_name:
            return redirect(url_for("hello_user", name=user_name))
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
