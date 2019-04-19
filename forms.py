from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, Email, AnyOf, NumberRange, URL
from flask_debugtoolbar import DebugToolbarExtension

class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[('dog', 'Dog'), ('porcupine', 'Porcupine'), ('cat', 'Cat')], validators=[InputRequired()])
    photo_url = StringField("Photo URL", validators=[Optional(), URL(require_tld=True)])
    age = IntegerField("Age", validators=[InputRequired(), NumberRange(0, 30)])
    notes = TextAreaField("Notes", validators=[Optional()])
    

class EditPetForm(FlaskForm):
    photo_url = StringField("Photo URL", validators=[Optional(), URL(require_tld=True)])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Available")
    