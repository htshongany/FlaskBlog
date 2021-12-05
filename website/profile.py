from flask import Blueprint , render_template ,  abort , request , redirect , url_for
from flask_login import login_required , current_user

profile = Blueprint('profile', __name__)

@profile.route("/")
@login_required
def user_profile():

	title = f"user | {current_user.username} " 

	return render_template("profile/profile.html" , user=current_user , title=title)



@profile.route("/update/")
@login_required
def user_update():

	title = f"user | {current_user.username} " 

	return render_template("profile/profile.html" , user=current_user , title=title)