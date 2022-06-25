from django.contrib import admin
from blog.models import Post, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title',)
    raw_id_fields = ('author', 'likes', 'tags',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text',)
    raw_id_fields = ('post', 'author',)


admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)
