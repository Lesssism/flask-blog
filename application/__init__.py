from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def index():
   posts = [
      {
         'title': '标题1',
         'body': '这是第1篇推文的内容'
      },
      {
         'title': '标题2',
         'body': '这是第2篇推文的内容'
      },
      {
         'title': '标题3',
         'body': '这是第3篇推文的内容'
      }
   ]
   return render_template('index.html', posts=posts)


@app.route('/about')
def about():
   return render_template('about.html')