from flask import Flask, render_template,url_for

app = Flask(__name__)

@app.route("/")
def home1():
    return render_template('index.html')

@app.route("/home")
def home2():
    return render_template('index.html')

@app.route("/news")
def news():
    return render_template('news.html')

@app.route("/blogs")
def blogs():
    return render_template('blogs.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)