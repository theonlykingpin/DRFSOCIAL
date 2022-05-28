from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _
from utils.general_model import GeneralModel


User = get_user_model()


class SocialLink(GeneralModel):
    user = models.ForeignKey(
        to=User,
        verbose_name=_('User'),
        on_delete=models.CASCADE,
        related_name='social_links'
    )
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=128
    )
    url = models.URLField(
        verbose_name=_('Url')
    )

    class Meta:
        verbose_name = _('SocialLink')
        verbose_name_plural = _('SocialLinks')

    def __str__(self):
        return self.name
