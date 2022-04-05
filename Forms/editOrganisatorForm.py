from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import BooleanField, StringField, TextAreaField, HiddenField
from wtforms.fields import DecimalField

class EditOrganisatorForm(FlaskForm):
    OrganisationID = HiddenField("OrganisationID")
    Anschrift = StringField("Preisgeld")
    Name = StringField("Name")
    Sponsoren = StringField("Sponsoren")
    Telefonnummer = DecimalField("Telefonnummer")