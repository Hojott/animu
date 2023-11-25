from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField

class CandidateForm(FlaskForm):
    name = StringField("Candidate name")
    url = StringField("Candidate URL, e.g. Aniwave page")
 
    class Meta:
        csrf = False

class EditForm(FlaskForm):
    name = StringField("Candidate name")
    url = StringField("Candidate URL")
    selected = BooleanField("Selected")
    
    class Meta:
        csrf = False
