from django.contrib import admin
from post.admin.comment import CommentAdmin
from post.admin.post import PostAdmin
from post.models import Post, Comment

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
