from django.contrib import admin
from tag.admin.tag import TagAdmin
from tag.models import Tag

admin.site.register(Tag, TagAdmin)
