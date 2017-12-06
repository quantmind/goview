from flask import Blueprint, render_template, abort


web = Blueprint('web', __name__, template_folder='templates')
PAGES = ('index',)


@web.route('/', defaults={'page': 'index'})
def show(page):
    if page in PAGES:
        return render_template('home.html')
    abort(404)
