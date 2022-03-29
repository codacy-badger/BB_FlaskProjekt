from flask import Flask,request
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from models import db, Marathonlauf

marathonlauf_blueprint = Blueprint('marathonlauf_blueprint', __name__)

@marathonlauf_blueprint.route("/marathonlauf")
def index():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    marathonlauf = session.query(Marathonlauf).all()
    return render_template("laufer.html", items = marathonlauf)