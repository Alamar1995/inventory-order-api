from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    Extends the default Django User model.

    We use 'username' as the unique identifier and add 'is_admin' for
    role-based access control (RBAC).
    """
    # Inherits fields like:
    # id (PK)
    # username (unique)
    # password (hashed)
    # is_active, date_joined, etc.

    # is_admin (Boolean): Use the default 'is_staff' or 'is_superuser'
    # fields provided by AbstractUser, but we'll add 'is_admin'
    # explicitly if we need finer control separate from staff status.

    # We will use the built-in 'is_staff' for Admin status
    is_admin = models.BooleanField(
        default=False,
        help_text='Designates whether the user can manage inventory.'
    )

    def __str__(self):
        return self.username