from flask import Flask, render_template

#(Flask instances
app = Flask(__name__)

# route decorator
@app.route('/')

def index():
    first_name = "John"
    return render_template("index.html", first_name=first_name)


@app.route('/user/<name>')

def user(name):
    return render_template("user.html", name=name)

#Invalid page error
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#Internal server error
@app.errorhandler(500)
def page_not_found(e):
    return "render_template("500.html"), 500  