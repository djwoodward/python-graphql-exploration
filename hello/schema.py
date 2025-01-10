import graphene

from graphene_django.types import DjangoObjectType
from .models import Book

class BookType(DjangoObjectType):
    class Meta:
        model = Book

class Query(graphene.ObjectType):
    # Declare the 'books' field with the optional 'title' and 'author' arguments
    books = graphene.List(
        BookType,
        title=graphene.String(required=False),
        author=graphene.String(required=False)
    )

    def resolve_books(self, info, title=None, author=None):
        # Filter books by title and/or author if provided
        books = Book.objects.all()
        
        if title:
            books = books.filter(title__icontains=title)
        
        if author:
            books = books.filter(author__icontains=author)
        
        return books

schema = graphene.Schema(query=Query)