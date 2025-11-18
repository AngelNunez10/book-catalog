from flask import Flask, render_template, request
import json

app = Flask(__name__)

with open("books.json", "r") as f:
    books = json.load(f)

@app.route("/")
def home():
    sort_by = request.args.get("sort")
    query = request.args.get("q", "").strip().lower()

    filtered_books = books
    if query:
        filtered_books = [
            b for b in books
            if query in b["title"].lower()
            or query in b["author"].lower()
            or query in b["genre"].lower()
        ]

    if sort_by == "title":
        filtered_books = sorted(filtered_books, key=lambda b: b["title"])
    elif sort_by == "price":
        filtered_books = sorted(filtered_books, key=lambda b: b["price"])
    elif sort_by == "author":
        filtered_books = sorted(filtered_books, key=lambda b: b["author"])

    return render_template(
        "index.html",
        books=filtered_books,
        sort_by=sort_by,
        search_query=query,
    )

if __name__ == "__main__":
    app.run(debug=True)
