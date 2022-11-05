#
#
#

from flask import Blueprint, flash, render_template, request, session, url_for
from flask_login import login_user

from app.extensions import login_manager
from app.public.forms import LoginForm
from app.user.models import User
from app.utilities.url import redirect
from app.utilities.forms import flash_errors

blueprint = Blueprint('public', __name__, static_folder='../static')

#
#
#
@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(int(user_id))

#
#
#
@blueprint.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            login_user(form.user)
            return redirect('user.index')
        else:
            flash_errors(form)
    return render_template('public/index.html', form=form)
