from flask import Flask, request, redirect, flash
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from models import db, Organisator
from Forms.addOrganisator import AddOrganisatorForm
from Forms.deleteOrganisatorForm import DeleteOrganisatorForm
from Forms.editOrganisatorForm import EditOrganisatorForm

organisator_blueprint = Blueprint('organisator_blueprint', __name__)

@organisator_blueprint.route("/organisator", methods=["get","post"])
def index():
    
    addOrganisatorFormObject = AddOrganisatorForm()

    if addOrganisatorFormObject.validate_on_submit():
        print(addOrganisatorFormObject.Anschrift.data)
        print(addOrganisatorFormObject.Name.data)
        print(addOrganisatorFormObject.Sponsoren.data)
        print(addOrganisatorFormObject.Telefonnummer.data)

        newOrganisator = Organisator()
        newOrganisator.Anschrift = addOrganisatorFormObject.Anschrift.data
        newOrganisator.Name = addOrganisatorFormObject.Name.data
        newOrganisator.Sponsoren = addOrganisatorFormObject.Sponsoren.data
        newOrganisator.Telefonnummer = addOrganisatorFormObject.Telefonnummer.data

        db.session.add(newOrganisator)
        db.session.commit()

        return redirect("/organisator")

    marathonlauf = db.session.query(Organisator).all()
    return render_template("organisator.html", form = addOrganisatorFormObject, items = marathonlauf)

@organisator_blueprint.route("/organisator/delete", methods=["post"])
def deleteOrganisator():
    deleteOrganisatorFormObj = DeleteOrganisatorForm()
    if deleteOrganisatorFormObj.validate_on_submit():
        print("gültig")

        OrganisatorIdToDelete = deleteOrganisatorFormObj.OrganisationID.data
        OrganisatorToDelete = db.session.query(Organisator).filter(Organisator.OrganisationID == OrganisatorIdToDelete)
        OrganisatorToDelete.delete()
        
        db.session.commit()
    else:
        print("Fatal Error")
    
    flash(f"Organisator with id {OrganisatorIdToDelete} has been deleted")    

    return redirect("/organisator")

@organisator_blueprint.route("/organisator/editOrganisatorForm", methods=["post"])
def submitEditForm():
    editOrganisatorFormObject = EditOrganisatorForm()

    if editOrganisatorFormObject.validate_on_submit():
        print("Submit wurde durchgeführt")

        OrganisationID = editOrganisatorFormObject.OrganisationID.data

        Organisator_to_edit = db.session.query(Organisator).filter(Organisator.OrganisationID == OrganisationID).first()
        Organisator_to_edit.Anschrift = editOrganisatorFormObject.Anschrift.data
        Organisator_to_edit.Name = editOrganisatorFormObject.Name.data
        Organisator_to_edit.Sponsoren = editOrganisatorFormObject.Sponsoren.data
        Organisator_to_edit.Telefonnummer = editOrganisatorFormObject.Telefonnummer.data

        db.session.commit()

        return redirect("/organisator")
    else:
        raise ("Fatal Error")

@organisator_blueprint.route("/organisator/editMarathonlaufForm")
def showEditForm():
    OrganisationID = request.args["MarathonID"]

    Organisator_to_edit = db.session.query(Organisator).filter(Organisator.OrganisationID == OrganisationID).first()
    
    editOrganisatorFormObject = EditOrganisatorForm()

    editOrganisatorFormObject.MarathonID.data = Organisator_to_edit.MarathonID
    editOrganisatorFormObject.Preisgeld.data = Organisator_to_edit.Preisgeld
    editOrganisatorFormObject.Kilometer.data = Organisator_to_edit.Kilometer
    editOrganisatorFormObject.Datum.data = Organisator_to_edit.Datum
    editOrganisatorFormObject.Preis_für_Teilnahme.data = Organisator_to_edit.Preis_für_Teilnahme
    editOrganisatorFormObject.Besucher.data = Organisator_to_edit.Besucher
    
    return render_template("editMarathonlaufForm.html", form = editOrganisatorFormObject)