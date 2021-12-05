from os import path
import re
import os


DB_NAME = "sqlite3.db"

def appconfig(app):

	app.config["SECRET_KEY"] = "R*J^Jb#j5qAT2_ELgtpA?bx**tKvq8j3"
	app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
	app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True



def create_database(app , db):
	if not os.path.exists(f'website/{DB_NAME}'):
		db.create_all(app=app)
		print("Created Database")

def check_password(password):
	if (len(password)<8):
		return True, "password is short"
	elif not re.search("[a-z]", password):
		return True ,"the password must contain a lowercase"
	elif not re.search("[A-Z]", password):
		return True ,"the password must contain a capital letter"
	elif not re.search("[0-9]", password):
		return True ,"the password must contain a number"
	elif re.search("\s", password):
		return True ,"the password must not contain spaces "
	else:
		return False , "success"
