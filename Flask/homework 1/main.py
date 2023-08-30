from flask import Flask, render_template

app= Flask(__name__)

@app.route("/main/")
def main_page():
    return render_template("index.html", **{"title":'Main'})

@app.route("/")
def main():
    content={"title":'main'}
    return render_template("index.html", **content)


@app.route("/clothes/")
def clothes():
    content={"title":'Clothes'}
    return render_template("clothes.html", **content)


@app.route("/boots/")
def boots():
    content={"title":'Boots'}
    return render_template("boots.html", **content)


@app.route("/jackets/")
def jackets():
    content={"title":'Jackets'}
    return render_template("jackets.html", **content)


if __name__=='__main__':
    app.run()