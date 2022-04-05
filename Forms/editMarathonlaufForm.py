from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import BooleanField, StringField, TextAreaField, HiddenField
from wtforms.fields import DecimalField

class EditMarathonlaufrForm(FlaskForm):
    MarathonID = HiddenField("MarathonID")
    Preisgeld = DecimalField("Preisgeld")
    Kilometer = DecimalField("Kilometer")
    Datum = DateField("Datum")
    Preis_für_Teilnahme = DecimalField("Preis_für_Teilnahme")
    Besucher = DecimalField("Besucher")