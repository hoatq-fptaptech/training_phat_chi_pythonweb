from flask import Flask, render_template,request,redirect
import db
app = Flask(__name__)  # tạo ta 1 object Flask -> là package tạo ra 1ứng đụng website

@app.route('/')
def index():
    # get data category
    data = db.read_data("select * from categories")
    categories = []
    for i in range(0, len(data["id"])):
        cat = {
            "id": data["id"][i],
            "name": data["name"][i],
        }
        categories.append(cat)

        # get data from posts -> render
    data2 = db.read_data("select * from posts limit 6")
    posts = []
    for i in range(0, len(data2["id"])):
        p = {
            "id": data2["id"][i],
            "title": data2["title"][i],
            "content": data2["content"][i],
            "created_at": data2["created_at"][i],
            "thumbnail": data2["thumbnail"][i],
            "author": data2["author"][i]
        }
        posts.append(p)
    return render_template("index.html", categories=categories,posts=posts)

@app.route('/about.html')
def hello():
    return render_template("about.html")

@app.route('/single.html/<id>')
def single(id):
    data = db.read_data(f"select * from posts where id={id}")
    post = {
        "id": data["id"][0],
        "title": data["title"][0],
        "content": data["content"][0],
        "created_at": data["created_at"][0],
        "thumbnail": data["thumbnail"][0],
        "author": data["author"][0]
    }
    return render_template("single.html",post=post)
#
@app.route('/create-post')
def create_post():
    return render_template("form.html")

@app.route('/save',methods=['POST'])
def save():
    post = {
        "title": request.form["title"],
        "content": request.form["content"],
        "author": request.form["author"],
    }
    db.insert_post(post)
    return redirect("/")