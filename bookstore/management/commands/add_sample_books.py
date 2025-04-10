from django.core.management.base import BaseCommand
from bookstore.models import Book

class Command(BaseCommand):
    help = 'Adds sample books to the database'

    def handle(self, *args, **options):
        sample_books = [
            {
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",
                "description": "A story of wealth, love, and the American Dream in the 1920s.",
                "price": 12.99,
                "stock": 50
            },
            
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "description": "A story of wealth, love, and the American Dream in the 1920s.",
        "price": 12.99,
        "stock": 50
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "description": "A powerful story of racial injustice and moral growth in the American South.",
        "price": 10.99,
        "stock": 45
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "description": "A dystopian novel about totalitarianism and surveillance.",
        "price": 9.99,
        "stock": 60
    },
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "description": "A romantic novel about the Bennett family and their quest for suitable marriages.",
        "price": 8.99,
        "stock": 40
    },
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "description": "A fantasy novel about Bilbo Baggins and his adventure to reclaim treasure.",
        "price": 14.99,
        "stock": 55
    },
    {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "description": "A novel about teenage rebellion and alienation.",
        "price": 11.99,
        "stock": 35
    },
    {
        "title": "The Lord of the Rings",
        "author": "J.R.R. Tolkien",
        "description": "An epic fantasy trilogy about the quest to destroy the One Ring.",
        "price": 29.99,
        "stock": 30
    },
    {
        "title": "Harry Potter and the Philosopher's Stone",
        "author": "J.K. Rowling",
        "description": "The first book in the Harry Potter series about a young wizard.",
        "price": 13.99,
        "stock": 70
    },
    {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "description": "A philosophical book about a shepherd's journey to find his treasure.",
        "price": 10.99,
        "stock": 65
    },
    {
        "title": "Brave New World",
        "author": "Aldous Huxley",
        "description": "A dystopian novel about a futuristic society based on science and efficiency.",
        "price": 9.99,
        "stock": 40
    }
        ]

        created_count = 0
        for book_data in sample_books:
            _, created = Book.objects.get_or_create(
                title=book_data['title'],
                defaults=book_data
            )
            if created:
                created_count += 1

        self.stdout.write(self.style.SUCCESS(
            f'Successfully added {created_count} sample books. ' 
            f'Skipped {len(sample_books) - created_count} existing books.'
        ))