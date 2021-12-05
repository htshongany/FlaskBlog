from flask import Blueprint , render_template , abort
from flask_login import login_required , current_user
from website.models import User , Article
views = Blueprint("views", __name__)



@views.route("/")
# @login_required
def home():
	title = "home"
	# article = Article.query.filter_by(user_id=current_user.id).all()
	return render_template("views/home.html", title=title , user=current_user)

@views.route("/about")
def about():
	title = "about"
	return render_template("views/about.html", title=title , user=current_user)


