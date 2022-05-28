from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _
from utils import GeneralModel
from utils.snippets import change_file_extension_user


class User(AbstractUser, GeneralModel):
    email = models.EmailField(
        _('email address'),
        unique=True,
        error_messages={
            'null': _('User must have an email address'),
            'blank': _('User must have an email address'),
            'invalid': _('Invalid email address'),
            'unique': _('This email is already in use')
        },
        help_text=_('Enter a valid email address')
    )
    email_verified = models.BooleanField(
        _('Email Verified'),
        default=False,
        help_text=_('Email Verified')
    )
    cover = models.ImageField(
        _('Cover'),
        upload_to=change_file_extension_user,
        null=True,
        blank=True,
        help_text=_('Cover')
    )
    main_image = models.CharField(
        _('Main Image'),
        max_length=1024,
        null=True,
        blank=True,
        unique=True,
        help_text=_('Main Image')
    )
    description = models.TextField(
        _('Description'),
        max_length=1024,
        null=True,
        blank=True,
        help_text=_('Description')
    )
    followers = models.ManyToManyField(
        to='user.User',
        verbose_name=_('Followers'),
        related_name='user_followers',
        blank=True,
        help_text=_('Followers')
    )
    following = models.ManyToManyField(
        to='user.User',
        verbose_name=_('Following'),
        related_name='user_following',
        blank=True,
        help_text=_('Following')
    )
    follower_count = models.PositiveIntegerField(
        _('Total Follower'),
        default=0,
        null=True,
        blank=True,
        help_text=_('Total Follower')
    )
    following_count = models.PositiveIntegerField(
        _('Total Following'),
        default=0,
        null=True,
        blank=True,
        help_text=_('Total Following')
    )
    post_count = models.PositiveIntegerField(
        _('Total post'),
        default=0,
        null=True,
        blank=True,
        help_text=_('Total post')
    )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
