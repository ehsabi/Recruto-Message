from flask import Blueprint, render_template, request

views = Blueprint(__name__ , "views") 

@views.route("/")
def home():
    args = request.args
    name = args.get('name')
    message= args.get('message')
    return render_template("index.html", name=name, message=message)

                           


