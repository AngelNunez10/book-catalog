from decimal import Decimal
import boto3

dynamodb = boto3.resource("dynamodb", region_name="us-east-1") 
table = dynamodb.Table("Products")

books = [
    {
        "productId": "22222222-2222-2222-2222-222222222222",
        "name": "Dune",
        "author": "Frank Herbert",
        "genre": "Science Fiction",
        "description": "A science fiction epic set on the desert planet Arrakis.",
        "price": Decimal("15.0"),
        "imageKey": "images/dune.jpg",
        "tags": ["science-fiction", "classic", "bestseller"],
    },
    {
        "productId": "11111111-1111-1111-1111-111111111111",
        "name": "Flowers for Algernon",
        "author": "Daniel Keyes",
        "genre": "Science Fiction",
        "description": "A psychological science fiction story about Charlie Gordon, who undergoes an experimental procedure to increase his intelligence.",
        "price": Decimal("9.99"),
        "imageKey": "images/flowers-for-algernon.jpg",
        "tags": ["science-fiction", "psychological", "classic"],
    },
    {
        "productId": "33333333-3333-3333-3333-333333333333",
        "name": "The Hunger Games",
        "author": "Suzanne Collins",
        "genre": "Dystopian",
        "description": "A dystopian novel where Katniss Everdeen volunteers to take her sister's place in a deadly televised competition.",
        "price": Decimal("12.50"),
        "imageKey": "images/the-hunger-games.jpg",
        "tags": ["dystopian", "young-adult", "bestseller"],
    },
    {
        "productId": "44444444-4444-4444-4444-444444444444",
        "name": "1984",
        "author": "George Orwell",
        "genre": "Dystopian",
        "description": "A dystopian novel exploring surveillance, totalitarianism, and the suppression of truth.",
        "price": Decimal("10.99"),
        "imageKey": "images/1984.jpg",
        "tags": ["dystopian", "classic", "political"],
    },
    {
        "productId": "55555555-5555-5555-5555-555555555555",
        "name": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Classic",
        "description": "A novel exploring racial injustice and moral growth in the American South.",
        "price": Decimal("11.99"),
        "imageKey": "images/to-kill-a-mockingbird.jpg",
        "tags": ["classic", "historical", "coming-of-age"],
    },
    {
        "productId": "66666666-6666-6666-6666-666666666666",
        "name": "Pride and Prejudice",
        "author": "Jane Austen",
        "genre": "Romance",
        "description": "A beloved classic exploring love, marriage, and social class through Elizabeth Bennet and Mr. Darcy.",
        "price": Decimal("8.50"),
        "imageKey": "images/pride-and-prejudice.jpg",
        "tags": ["classic", "romance", "literature"],
    },
    {
        "productId": "77777777-7777-7777-7777-777777777777",
        "name": "Crime and Punishment",
        "author": "Fyodor Dostoevsky",
        "genre": "Philosophical Fiction",
        "description": "A psychological novel exploring morality, guilt, and redemption through Raskolnikov's crime.",
        "price": Decimal("14.00"),
        "imageKey": "images/crime-and-punishment.jpg",
        "tags": ["classic", "philosophical", "psychological"],
    },
    {
        "productId": "88888888-8888-8888-8888-888888888888",
        "name": "Fahrenheit 451",
        "author": "Ray Bradbury",
        "genre": "Dystopian",
        "description": "In a future society, books are banned and firemen burn them to suppress knowledge and freedom.",
        "price": Decimal("9.50"),
        "imageKey": "images/fahrenheit-451.jpg",
        "tags": ["dystopian", "classic", "political"],
    },
    {
        "productId": "99999999-9999-9999-9999-999999999999",
        "name": "The Humans",
        "author": "Matt Haig",
        "genre": "Science Fiction",
        "description": "An alien takes over a mathematician's body and discovers the beauty and complexity of human life.",
        "price": Decimal("13.75"),
        "imageKey": "images/the-humans.jpg",
        "tags": ["science-fiction", "philosophical", "humor"],
    },
    {
        "productId": "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
        "name": "The Martian",
        "author": "Andy Weir",
        "genre": "Science Fiction",
        "description": "Astronaut Mark Watney must survive alone on Mars using engineering ingenuity and determination.",
        "price": Decimal("14.99"),
        "imageKey": "images/the-martian.jpg",
        "tags": ["science-fiction", "survival", "adventure"],
    },
]


def main():
    with table.batch_writer() as batch:
        for book in books:
            if not isinstance(book["price"], Decimal):
                raise TypeError(f"price for {book['name']} is not Decimal: {type(book['price'])}")
            batch.put_item(Item=book)
            print(f"Inserted: {book['name']}")


if __name__ == "__main__":
    print("Seeding DynamoDB with book data...")
    main()
    print("Done!")
