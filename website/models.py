from flask_login import UserMixin
from datetime import datetime
from .import db 

class User(db.Model, UserMixin):

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(150) , nullable=False)
	image_file = db.Column(db.String(20),nullable=False, default='profile.png')
	email = db.Column(db.String(150) , nullable=False ,unique=True)
	password = db.Column(db.String(150) , nullable=False)

	is_active = db.Column(db.Boolean(), nullable=False, default=True)
	admin = db.Column(db.Boolean(), nullable=False, default=False)
	# status 

	article = db.relationship("Article" , backref='author', lazy=True)

	def __repr__(self):
		return f"{self.email} | {self.username} | {self.password} | {self.is_active} "

# group
# manytomany

class Article(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(150),nullable=False)
	content = db.Column(db.String(5000),nullable=False)
	post_date = db.Column(db.DateTime(timezone=True), default=datetime.utcnow())
	available = db.Column(db.Boolean(), nullable=False, default=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return f" id : {self.id} | title : {self.title} | at : {self.post_date} | {self.content} | {self.user_id} "


# tag 
# manytomany avec article 