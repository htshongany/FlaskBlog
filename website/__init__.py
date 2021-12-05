from flask import Flask
from flask.helpers import url_for 
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flaskext.markdown import Markdown
from .utils import appconfig , create_database


db = SQLAlchemy()

def create_app():
	app = Flask(__name__)

	# app configuration 
	appconfig(app)

	Markdown(app)

	# database initialisation 
	db.init_app(app)
	
	# import bleuprint
	from .views import views
	from .auth import auth
	from .posts import posts
	from .profile import profile
	from .errors import error_404 , error_500 , error_403

	app.register_blueprint(views, url_prefix='/')
	app.register_blueprint(profile, url_prefix='/profile/')
	app.register_blueprint(auth,url_prefix='/auth/')
	app.register_blueprint(posts,url_prefix='/post/' )
	
	error_404(app)
	error_500(app)
	error_403(app)

	# database
	from .models import User
	create_database(app , db)


	login_manager = LoginManager()
	login_manager.login_view = 'auth.login'
	login_manager.init_app(app)

	@login_manager.user_loader
	def load_user(id):
		return User.query.get(int(id))

	
	return app

