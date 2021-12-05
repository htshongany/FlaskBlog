from flask import  render_template
from flask_login import current_user

def error_404(app):
	@app.errorhandler(404)
	def resource_not_found(e):
	    return render_template('errors/404.html', user=current_user), 404


def error_500(app):
	@app.errorhandler(500)
	def func(e):
		return render_template('errors/500.html', user=current_user) , 500


def error_403(app):
	@app.errorhandler(403)
	def func(e):
		return render_template('errors/403.html',user=current_user), 403
		
