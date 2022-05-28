from django.contrib import admin


class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'url']
    list_filter = ['user', 'name', 'url']
    search_fields = ['user', 'name', 'url']
