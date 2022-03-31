from flask import Flask, request, redirect
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from models import db, Marathonlauf
from Forms.addMarathonlaufForm import AddMarathonlaufForm

marathonlauf_blueprint = Blueprint('marathonlauf_blueprint', __name__)

@marathonlauf_blueprint.route("/marathonlauf", methods=["get","post"])
def index():

    addMarathonlaufFormObject = AddMarathonlaufForm()

    if addMarathonlaufFormObject.validate_on_submit():
        print(addMarathonlaufFormObject.Preisgeld.data)
        print(addMarathonlaufFormObject.Kilometer.data)
        print(addMarathonlaufFormObject.Datum.data)
        print(addMarathonlaufFormObject.Preis_für_Teilnahme.data)
        print(addMarathonlaufFormObject.Besucher.data)

        newMarathonlauf = Marathonlauf()
        newMarathonlauf.Preisgeld = addMarathonlaufFormObject.Preisgeld.data
        newMarathonlauf.Kilometer = addMarathonlaufFormObject.Kilometer.data
        newMarathonlauf.Datum = addMarathonlaufFormObject.Datum.data
        newMarathonlauf.Preis_für_Teilnahme = addMarathonlaufFormObject.Preis_für_Teilnahme.data
        newMarathonlauf.Besucher = addMarathonlaufFormObject.Besucher.data

        db.session.add(newMarathonlauf)
        db.session.commit()

        return redirect("/marathonlauf")

    marathonlauf = db.session.query(newMarathonlauf).all()
    return render_template("marathonlauf.html", form = AddMarathonlaufForm, items = marathonlauf)