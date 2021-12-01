from django.db import models
from django.utils.translation import gettext_lazy as _


class LibraryUserType(models.TextChoices):
    ADMIN = 'AD', _('Admin')
    READER = 'RD', _('Reader')
    LIBRARIAN = 'LI', _('Librarian')
    CLEANERS = 'CL', _('Cleaners')
    STAFF = 'ST', _('Staff')
    SECURITY = 'SC', _('Security')
    THIRD_PARTY = 'TP', _('Third Party')


class Accessibility(models.Model):
    acb1 = models.CharField(default=60)
    user_type = models.CharField(
        max_length=2,
        choices=LibraryUserType.choices,
        default=LibraryUserType.READER
    )


class Users(models.Model):
    name = models.CharField(max_length=60)
    library_staff = models.CharField(
        max_length=2,
        choices=LibraryUserType.choices,
        default=LibraryUserType.READER
    )

    def __str__(self):
        return self.name

