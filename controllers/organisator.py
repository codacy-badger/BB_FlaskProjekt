from flask import Flask, request, redirect
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from models import db, Organisator
from Forms.addOrganisator import AddOrganisatorForm

organisator_blueprint = Blueprint('organisator_blueprint', __name__)

@organisator_blueprint.route("/organisator")
def index():
    
    addOrganisatorFormObject = AddOrganisatorForm()

    if addOrganisatorFormObject.validate_on_submit():
        print(addOrganisatorFormObject.Preisgeld.data)
        print(addOrganisatorFormObject.Kilometer.data)
        print(addOrganisatorFormObject.Datum.data)
        print(addOrganisatorFormObject.Preis_für_Teilnahme.data)
        print(addOrganisatorFormObject.Besucher.data)

        newMarathonlauf = Organisator()
        newMarathonlauf.Preisgeld = addOrganisatorFormObject.Preisgeld.data
        newMarathonlauf.Kilometer = addOrganisatorFormObject.Kilometer.data
        newMarathonlauf.Datum = addOrganisatorFormObject.Datum.data
        newMarathonlauf.Preis_für_Teilnahme = addOrganisatorFormObject.Preis_für_Teilnahme.data
        newMarathonlauf.Besucher = addOrganisatorFormObject.Besucher.data

        db.session.add(newMarathonlauf)
        db.session.commit()

        return redirect("/marathonlauf")

    marathonlauf = db.session.query(Marathonlauf).all()
    return render_template("marathonlauf.html", form = AddMarathonlaufForm, items = marathonlauf)