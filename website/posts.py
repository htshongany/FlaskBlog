from flask import Blueprint , render_template ,  abort , request , redirect , url_for
from . import db
from .models import User , Article
from flask_login import login_required , current_user

posts = Blueprint('posts', __name__)

# Article | Article

# list article 
@posts.route("/")
def article_list():
	title = "Articles"
	article = Article.query.all()
	return render_template("post/list.html", title=title , user=current_user ,articles=article )

# detail

@posts.route("/<int:id>/")
@login_required
def article_detail(id):
	title = "Article detail"
	article = Article.query.get_or_404(id)

	return render_template("post/detail.html", title=title , user=current_user ,article=article )
	


# update article 
@posts.route("/update/<int:id>/" , methods=["POST","GET"])
@login_required
def article_update(id):
	
	article = Article.query.get_or_404(id)
	if (article.user_id != current_user.id):
		return abort(403)

	title = f"update Article | {article.title}"

	if request.method == "POST":
		article.title = request.form.get('article-title') 
		article.content = request.form.get('article-content')
		# article.content = request.form.get('editordata')
		available = request.form.get('available')

		if available:
			article.available = True
		else:
			article.available = False

		 
		try:
			db.session.commit()
			print(article.available)
			return redirect(url_for('posts.article_detail',id=article.id)) 
		except Exception as e:
			return abort(500)

	return render_template("post/update.html", title=title , user=current_user ,article=article )
	
		


# delete article

@posts.route("/delete/<int:id>/" , methods=["POST","GET"])
@login_required
def delete_article(id):

	article = Article.query.get_or_404(id)
	title = f"delete | {article.title}"
	if (article.user_id == current_user.id):
		if request.method == "POST":
			db.session.delete(article)
			db.session.commit()
			return redirect(url_for('posts.article_list'))
		return render_template("post/delete.html", title=title , user=current_user ,article=article )
	else:
		return abort(403)
	

# add article 
@posts.route("/add/" , methods=["POST","GET"])
@login_required
def add_article():
	title = "add Article"

	if request.method == "POST":
		title = request.form.get('article-title')
		content = request.form.get('article-content')
		available = request.form.get('available')

		if available:
			available = True
		else:
			available = False
			
		add_article = Article(title=title , content=content ,available=available, user_id=current_user.id)

		print(add_article.available)
		
		if (add_article.available == None and add_article.content == None) or add_article.title == None:
			return abort(500)
		

		db.session.add(add_article)
		db.session.commit()

		return redirect(url_for('posts.article_detail',id=add_article.id)) 
		return redirect(url_for('posts.article_list'))


	return render_template("post/add.html", title=title , user=current_user)