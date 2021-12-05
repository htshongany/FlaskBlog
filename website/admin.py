from flask import Blueprint , render_template
from flask_login import login_required , current_user

admin = Blueprint('admin', __name__)

