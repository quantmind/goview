import os

from flask import Blueprint, render_template, abort

from .config import PATH, VERSION


web = Blueprint('web', __name__, template_folder='templates')
PAGES = ('index',)


@web.route('/template/<component>', defaults={'name': 'template'})
def component(component, name):
    location = os.path.join(
        PATH, 'ui', 'components', component, '%s.html' % name
    )
    if os.path.isfile(location):
        with open(location, 'r') as fp:
            return fp.read()
    abort(404)


@web.route('/', defaults={'page': 'index'})
def show(page):
    if page in PAGES:
        return render_template('home.html', version=VERSION.replace('.', '-'))
    abort(404)
