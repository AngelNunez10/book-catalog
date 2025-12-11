from flask import Flask, render_template, request
from decimal import Decimal
import boto3

app = Flask(__name__)

dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
table = dynamodb.Table("Products")

def convert_decimals(obj):

    if isinstance(obj, list):
        return [convert_decimals(x) for x in obj]
    elif isinstance(obj, dict):
        return {k: convert_decimals(v) for k, v in obj.items()}
    elif isinstance(obj, Decimal):
        return float(obj)
    else:
        return obj

def get_books_from_dynamodb():

    resp = table.scan()
    items = resp.get("Items", [])

    items = convert_decimals(items)

    adapted = []
    for item in items:
        book = dict(item)

        if "name" in book and "title" not in book:
            book["title"] = book["name"]
        adapted.append(book)

    return adapted

@app.route("/")
def home():
    sort_by = request.args.get("sort")
    query = request.args.get("q", "").strip().lower()

    books = get_books_from_dynamodb()

    filtered_books = books
    if query:
        filtered_books = [
            b for b in books
            if query in b.get("title", "").lower()
            or query in b.get("author", "").lower()
            or query in b.get("genre", "").lower()
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
