from flask import Flask,request
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from models import db, Marathon

organisator_blueprint = Blueprint('laufer_blueprint', __name__)

@organisator_blueprint.route("/laufer")
def index():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    organisator = session.query(Marathon).all()
    return render_template("laufer.html", items = organisator)