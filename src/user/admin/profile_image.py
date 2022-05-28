from django.contrib import admin


class ProfileImageAdmin(admin.ModelAdmin):
    list_display = ['user', 'image']
    list_filter = ['user', 'image']
    search_fields = ['user', 'image']
