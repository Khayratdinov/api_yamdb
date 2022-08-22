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

    first_name = models.CharField(
                                  max_length=150,
                                  blank=True,
                                  null=True,
    )
    last_name = models.CharField(
                                 max_length=150,
                                 blank=True,
                                 null=True,
    )

    bio = models.TextField(
                            blank=True,
                            null=True,
                            help_text='User biography',
    )

    role = models.TextField(
                            choices=RoleChoice.choices,
                            default=RoleChoice.USER,
                            help_text='Role user',
    )

    confirmation_code = models.CharField(
                                         max_length=255,
                                         null=True,
                                         blank=False,
    )


    @property
    def is_user(self):
        return self.role == RoleChoice.USER

    @property
    def is_admin(self):
        return self.role == RoleChoice.ADMIN

    @property
    def is_moderator(self):
        return self.role == RoleChoice.MODERATOR


    class Meta:
        ordering = ('username',)

    def __str__(self) -> str:
        return self.username