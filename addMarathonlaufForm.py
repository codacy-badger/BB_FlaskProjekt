from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import StringField
from wtforms import validators

class AddMarathonlaufForm(FlaskForm):
    Preisgeld = int("Preisgeld")
    Kilometer = int("Kilometer")
    Datum = DateField("Datum")
    Preis_für_Teilnahme = int("Preis_für_Teilnahme")
    Besucher = StringField("Besucher",validators=[validators.InputRequired()])