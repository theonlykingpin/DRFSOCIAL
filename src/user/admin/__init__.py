from django.contrib import admin
from user.admin.activation_code import ActivationCodeAdmin
from user.admin.profile_image import ProfileImageAdmin
from user.admin.social_link import SocialLinkAdmin
from user.admin.user import MyUserAdmin
from user.models import ActivationCode, ProfileImage, SocialLink, User


admin.site.register(ActivationCode, ActivationCodeAdmin)
admin.site.register(ProfileImage, ProfileImageAdmin)
admin.site.register(SocialLink, SocialLinkAdmin)
admin.site.register(User, MyUserAdmin)
