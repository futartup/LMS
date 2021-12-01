from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=60, unique=True)
    # It can be FK to another table as Author
    author_name = models.CharField(max_length=60)
    isbn_num = models.CharField(max_length=60)
    genre = models.CharField(max_length=60)
    description = models.TextField()

    def __str__(self):
        return self.title
