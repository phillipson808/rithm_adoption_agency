from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Optional, Email, AnyOf
from flask_debugtoolbar import DebugToolbarExtension

class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[('dog', 'Dog'), ('porcupine', 'Porcupine'), ('cat', 'Cat')], validators=[InputRequired()])
    photo_url = StringField("Photo URL", validators=[Optional()])
    age = IntegerField("Age", validators=[InputRequired()])
    notes = TextAreaField("Notes", validators=[Optional()])

