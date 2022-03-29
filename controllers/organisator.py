from flask import Flask,request
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from models import db, Organisator

organisator_blueprint = Blueprint('organisator_blueprint', __name__)

@organisator_blueprint.route("/organisator")
def index():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    organisator = session.query(Organisator).all()
    return render_template("laufer.html", items = organisator)