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
        print(addOrganisatorFormObject.Anschrift.data)
        print(addOrganisatorFormObject.Name.data)
        print(addOrganisatorFormObject.Sponsoren.data)
        print(addOrganisatorFormObject.Telefonnummer.data)
        print(addOrganisatorFormObject.Besucher.data)

        newOrganisator = Organisator()
        newOrganisator.Anschrift = addOrganisatorFormObject.Anschrift.data
        newOrganisator.Name = addOrganisatorFormObject.Name.data
        newOrganisator.Sponsoren = addOrganisatorFormObject.Sponsoren.data
        newOrganisator.Telefonnummer = addOrganisatorFormObject.Telefonnummer.data
        newOrganisator.Besucher = addOrganisatorFormObject.Besucher.data

        db.session.add(newOrganisator)
        db.session.commit()

        return redirect("/organisator")

    marathonlauf = db.session.query(Organisator).all()
    return render_template("organisator.html", form = addOrganisatorFormObject, items = marathonlauf)