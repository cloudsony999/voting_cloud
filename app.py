from flask import Flask,render_template

app=Flask(__name__)

@app.route("/vote/<name>/<int:age>")
def hello(name,age):
    return render_template("vote.html",name=name,age=age)

@app.route("/")
def hello2():
    return render_template("bagan.html")


if __name__=='__main__':
    app.run()

    
