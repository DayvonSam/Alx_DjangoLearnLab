from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)        # Title of the book
    author = models.CharField(max_length=100)       # Author name
    publication_year = models.IntegerField()        # Year published

    def __str__(self):
        return self.title  # This makes the book readable in admin and shell
