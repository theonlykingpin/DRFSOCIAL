from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _
from utils import GeneralModel
from utils.snippets import change_file_extension_post

User = get_user_model()


class Post(GeneralModel):
    user = models.ForeignKey(
        to=User,
        verbose_name=_('Author'),
        on_delete=models.CASCADE,
        related_name='posts'
    )
    caption = models.TextField(
        verbose_name=_('Caption')
    )
    file = models.ImageField(
        verbose_name=_('Media'),
        upload_to=change_file_extension_post,
        max_length=128,
        null=True,
        blank=True
    )
    tag = models.ManyToManyField(
        to='tag.Tag',
        verbose_name=_('Tag'),
        blank=True
    )
    like = models.ManyToManyField(
        to=User,
        verbose_name=_('Like'),
        related_name='likers',
        blank=True
    )
    feed = models.ManyToManyField(
        to=User,
        verbose_name=_('Feed'),
        blank=True
    )
    reshare = models.ForeignKey(
        to='post.Post',
        verbose_name=_('Feed'),
        on_delete=models.CASCADE,
        related_name='reshares',
        null=True,
        blank=True,
        default=None
    )
    reshare_count = models.PositiveIntegerField(
        verbose_name=_('Total Reshare'),
        default=0
    )
    comment_count = models.PositiveIntegerField(
        verbose_name=_('Total Comment'),
        default=0
    )
    like_count = models.PositiveIntegerField(
        verbose_name=_('Total Like'),
        default=0
    )

    def __str__(self):
        return f'{self.user} {self.caption[:10]}'
