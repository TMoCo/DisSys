from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField

from webservice.apiRequests import locapi

class LocationForm(FlaskForm):
    choices = [(loc, loc) for loc in locapi.getCountryList()]

    origin = SelectField(u'locations', choices=choices)
    destination = SelectField(u'locations', choices=choices)
    submit = SubmitField('Let\'s go!')
