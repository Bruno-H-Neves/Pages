from flask import Flask

app=Flask(__name__)

@app.route("/")
def homepage():
    return "First Web Page"

@app.route("/contact")
def contact():
    return "<p>Contact:</p><p>Phonee:</p><p>Mail:</p><p>Github:</p><p>Linkdin:</p>"


if __name__=="__main__":
    app.run(debug=True)