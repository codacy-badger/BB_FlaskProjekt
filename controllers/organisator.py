from flask import Flask, request, redirect, flash
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from models import db, Organisator
from Forms.addOrganisator import AddOrganisatorForm
from Forms.deleteOrganisatorForm import DeleteOrganisatorForm

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

organisator_blueprint.route("/organisator/delete", methods=["post"])
def deleteOrganisator():
    deleteOrganisatorFormObj = DeleteOrganisatorForm()
    if deleteOrganisatorFormObj.validate_on_submit():
        print("gültig")

        OrganisatorIdToDelete = deleteOrganisatorFormObj.itemId.data
        OrganisatorToDelete = db.session.query(Organisator).filter(Organisator.MarathonID == OrganisatorIdToDelete)
        OrganisatorToDelete.delete()
        
        db.session.commit()
    else:
        print("Fatal Error")
    
    flash(f"Organisator with id {OrganisatorIdToDelete} has been deleted")    

    return redirect("/organisator")