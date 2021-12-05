from flask import Blueprint , render_template , request , flash , redirect ,url_for
from flask_login import login_user , login_required , logout_user , current_user
from werkzeug.security import  generate_password_hash , check_password_hash

from .utils import check_password

from .models import User
from . import db


auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["POST","GET"])
def login():

	if request.method == "POST":
		email = request.form.get('email')
		password = request.form.get('password')
		user = User.query.filter_by(email=email).first()

		if user:
			if check_password_hash(user.password , password):
				login_user(user, remember=True)
				flash("successful ", category="success")
				return redirect(url_for('profile.user_profile'))
			else:
				flash("your password is not correct" , category="error")
		else:
			flash("email does not exit " , category="error")

		

	return render_template("auth/login.html" , user=current_user)


@auth.route("/logout")
@login_required
def logout():
	logout_user()
	return redirect(url_for('auth.login'))

@auth.route("/sing-up" , methods=["POST","GET"])
def sing_up():
	title = "sing-up"

	if request.method == "POST":

		email = request.form.get('email')
		username = request.form.get('username')
		password1 = request.form.get('password1')
		password2 = request.form.get('password2')

		# controle
		user = User.query.filter_by(email=email).first()
		if user:
			flash("email alredy exist ...", 'error')

		elif  password1 != password2:
			flash("password must be equale to confime password", category='error')

		# elif len(password1) < 8:
		# 	flash("password is short" , category="error")

		elif True == check_password(password1)[0]:
			flash(check_password(password1)[1] ,  category="error")


		elif len(email) < 10:
			flash("email court ...", category='error')

		elif len(username) < 2:
			flash("username court ...", category='error')

		else:
			news_user = User(email=email,username=username, password=generate_password_hash(password1,method="sha256"), )
			db.session.add(news_user)
			db.session.commit()
			flash("success" , category='success')
			login_user(news_user, remember=True)
			return redirect(url_for('profile.user_profile'))
	
	return render_template("auth/sing_up.html" , user=current_user)