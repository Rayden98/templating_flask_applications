from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()

    title1 = all_posts[0]["title"]
    title2 = all_posts[1]["title"]

    subtitle1 = all_posts[0]["subtitle"]
    subtitle2 = all_posts[1]["subtitle"]

    return render_template("index.html", posts=all_posts, title1=title1, title2=title2, subtitle1=subtitle1, subtitle2=subtitle2)

@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()

    title1 = all_posts[int(num)]["title"]

    subtitle1 = all_posts[int(num)]["subtitle"]

    body1 = all_posts[int(num)]["body"]

    return render_template("post.html", posts=all_posts, title1=title1, subtitle1=subtitle1, body1=body1)

if __name__ == "__main__":
    app.run(debug=True)
