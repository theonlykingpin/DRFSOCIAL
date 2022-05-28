from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


class MyUserAdmin(UserAdmin):
    list_display = ("username", "email", "is_staff", 'is_active', 'is_superuser', 'email_verified', 'last_login')
    list_filter = ("is_active", "is_staff", "is_superuser", "groups", 'email_verified')
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "cover", "main_image", "description",
                                         "followers", "following", "follower_count", "following_count", "post_count")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "email_verified",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
