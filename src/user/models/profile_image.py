from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _
from utils.general_model import GeneralModel
from utils.snippets import change_file_extension_profile

User = get_user_model()


class ProfileImage(GeneralModel):
    user = models.ForeignKey(
        to=User,
        verbose_name=_('User'),
        on_delete=models.CASCADE,
        related_name='profile_images'
    )
    image = models.ImageField(
        verbose_name=_('Image'),
        upload_to=change_file_extension_profile,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _('ProfileImage')
        verbose_name_plural = _('ProfileImages')

    def __str__(self):
        return f'{self.user}'
