from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import StringField
from wtforms import validators

class Organisator(FlaskForm):
    Anschrift = StringField("Anschrift",validators=[validators.InputRequired()])
    Name =  StringField("Name",validators=[validators.InputRequired()])
    Sponsoren =  StringField("Sponsoren",validators=[validators.InputRequired()])
    Telefonnummer = int("Telefonnummer")