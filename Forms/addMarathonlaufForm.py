from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import BooleanField, StringField, TextAreaField
from wtforms import validators

class AddLauferForm(FlaskForm):
    Preisgeld = int("Preisgeld", validators=[validators.InputRequired()])
    Kilometer = int("Kilometer", validators=[validators.InputRequired()])
    Datum = DateField("dueDate", validators=[validators.InputRequired()])
    Preis_für_Teilnahme = int("Preisgeld", validators=[validators.InputRequired()])
    Besucher = StringField("Besucher", validators=[validators.InputRequired()])