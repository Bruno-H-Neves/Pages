from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contact")
def contact():
    return render_template("MyContact.html")

@app.route("/users/<user_name>")  #<> para ser dinamico
def usuarios(user_name):
    return render_template("Users.html", User_name=user_name)


if __name__=="__main__":
    app.run(debug=True)