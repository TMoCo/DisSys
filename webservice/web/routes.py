from flask import render_template, redirect, request, url_for
from webservice import app
from webservice.web.forms import LocationForm

from webservice.apiRequests import locapi, mymem, gmap

@app.route('/', methods=['GET'])
def select():
    form = LocationForm()
    return render_template('select.html', title='Select', form=form)

@app.route('/results', methods=['GET'])
def results():
    # create a big dictionary containing all the data needed when rendering
    # the template of the results page
    context = {
        'origin': request.args.get('origin'),
        'destination': request.args.get('destination')
        }

    context['distance'] = str(locapi.getMyDistance(locapi.getMyCapital(context['origin']),\
                                locapi.getMyCapital(context['destination'])))

    # get map
    context['verify'] = gmap.getMap(context['origin'],context['destination'])

    # translate in local language
    code = locapi.getMyLanguageCode(context['destination'])
    myText = 'Greetings traveller'
    if code == 'en':
        context['text'] = myText # translate english to english? no need
    else:
        context['text'] = mymem.getTranslation(code, myText)

    return render_template('results.html', title='Results', context = context)
