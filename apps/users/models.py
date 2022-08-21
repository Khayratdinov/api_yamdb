from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
# ============================================================================ #


# ================================ ROLE CHOICE =============================== #

class RoleChoice(models.TextChoices):

    USER = "User", _("User")
    MODERATOR = "Moderator", _("Moderator")
    ADMIN = "Admin", _("Admin")




# =================================== USER =================================== #
class User(AbstractUser):

    username = models.CharField(
        'Логин',
        max_length=150,
        unique=True,
        help_text='User name',
        validators=[
            RegexValidator(
                regex=r'^[\w.@+-]+',
                message=('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.')
            )
        ]
    )
    password = models.CharField(
        max_length=128,
        blank=True,
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
    )
    confirmation_code = models.CharField(
        blank=True,
        max_length=9,
        help_text='Confirmation code'
    )
    first_name = models.CharField(
        max_length=150,
        blank=True,
    )
    last_name = models.CharField(
        max_length=150,
        blank=True,
    )
    bio = models.TextField(
        blank=True,
        help_text='User biography',
    )
    role = models.TextField(
        'Role',
        choices=RoleChoice.choices,
        default=RoleChoice.USER,
        help_text='Role user',
    )

    class Meta:
        ordering = ('username',)

    def __str__(self) -> str:
        return self.username