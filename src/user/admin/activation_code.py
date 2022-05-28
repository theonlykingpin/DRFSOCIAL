from django.contrib import admin


class ActivationCodeAdmin(admin.ModelAdmin):
    list_display = ['user', 'type', 'code', 'retry', 'used']
    list_filter = ['user', 'type', 'code', 'retry', 'used']
    search_fields = ['user', 'type', 'code', 'retry', 'used']
