from django.db import models
from books.models import Books
from users.models import Users
from django.utils.translation import gettext_lazy as _
from datetime import datetime


class Library(models.Model):
    title = models.CharField(max_length=60)
    library_id = models.CharField(max_length=60)
    parent_library_id = models.ForeignKey("self", on_delete=models.DO_NOTHING, null=True, blank=True)
    address = models.TextField()

    def __str__(self):
        return self.title


class BookActivity(models.TextChoices):
    PRESENT = 'PR', _('Present')
    BORROWED = 'BR', _('Borrowed')
    REPAIR = 'RR', _('Repair')
    DECOMMISIONED = 'DC', _('Decommissioned')
    ARRIVING = 'AR', _('Arriving')


class LibraryActivities(models.Model):
    library_id = models.ForeignKey(Library, on_delete=models.DO_NOTHING)
    book_id = models.ForeignKey(Books, on_delete=models.DO_NOTHING)
    user_id = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    activity_type = models.CharField(
        max_length=2,
        choices=BookActivity.choices,
        default=BookActivity.PRESENT
    )
    checked_out_at = models.DateTimeField(default=datetime.now)
    checked_in_at = models.DateTimeField(default=datetime.now)




