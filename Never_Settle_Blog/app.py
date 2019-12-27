from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
	id = db.Column(db.Integer,primary_key = True)
	title = db.Column(db.String(100),nullable = False,default = 'N/A')
	content = db.Column(db.Text,nullable = False,default = 'N/A')
	author = db.Column(db.String(10),nullable = False,default = 'N/A')
	created = db.Column(db.DateTime, default=datetime.utcnow)

	def __repr__(self):
		return 'Blog Post' + str(self.id)
@app.route('/')
def index():
	return render_template('home.html')
@app.route('/posts',methods = ['GET','POST'])
def posts():
	if request.method == 'POST':
		title = request.form['title']
		content =  request.form['content']
		author = request.form['author']
		new_post = BlogPost(title = title,content = content,author = author)
		db.session.add(new_post)
		db.session.commit()
		return redirect('/posts')
	else:
		allposts = BlogPost.query.order_by(BlogPost.id).all()
		return render_template('post.html',posts = allposts,id = id)
@app.route('/posts/delete/<int:id>')
def delete(id):
	post = BlogPost.query.get_or_404(id)
	db.session.delete(post)
	db.session.commit()
	return redirect('/posts')

@app.route('/posts/edit/<int:id>',methods = ['GET','POST'])
def edit(id):
	post = BlogPost.query.get_or_404(id)
	if request.method == 'POST':
		post.title = request.form['title']
		post.content = request.form['content']
		post.author = request.form['author']
		db.session.commit()
		return redirect('/posts')
	else:
		return render_template('edit.html',post = post)

@app.route('/posts/new',methods = ['GET','POST'])
def newpost():
	if request.method == 'POST':
		post.title = request.form['title']
		post.content = request.form['content']
		post.author = request.form['author']
		new_post = BlogPost(title = title,content = content,author = author)
		db.session.add(new_post)
		db.session.commit()
		return redirect('/posts')
	else:
		return render_template('newpost.html')

if __name__ == '__main__':
	app.run(debug = True)