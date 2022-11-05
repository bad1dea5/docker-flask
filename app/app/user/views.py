#
#
#

from flask import Blueprint, flash, render_template
from flask_login import login_required, logout_user

from app.user.models import User
from app.utilities.url import redirect

blueprint = Blueprint('user', __name__, static_folder='../static', url_prefix='/user')

#
#
#
@blueprint.route('/')
@login_required
def index():
    return render_template('user/index.html')

#
#
#
@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Successfully logged out.', category='success')
    return redirect('public.index')
