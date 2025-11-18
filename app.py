import json
from flask import Flask, render_template, request

app = Flask(__name__)

# Load books from JSON file
with open("books.json") as f:
    books = json.load(f)

@app.route("/")
def home():
    sort_by = request.args.get("sort")
    sorted_books = books

    if sort_by == "title":
        sorted_books = sorted(books, key=lambda b: b["title"])
    elif sort_by == "price":
        sorted_books = sorted(books, key=lambda b: b["price"])
    elif sort_by == "author":
        sorted_books = sorted(books, key=lambda b: b["author"])

    return render_template("index.html", books=sorted_books)

if __name__ == "__main__":
    app.run(debug=True)
