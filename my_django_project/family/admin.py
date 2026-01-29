from django.contrib import admin
from .models import Post, Comment, Suggestion, Like

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_at', 'short_content', 'has_image')
    list_filter = ('created_at', 'author')
    search_fields = ('content', 'author__username')

    def short_content(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    
    def has_image(self, obj):
        return bool(obj.image)
    has_image.boolean = True

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at', 'short_content')
    list_filter = ('created_at', 'author')
    search_fields = ('content', 'author__username')

    def short_content(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content

@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('created_at', 'author')
    search_fields = ('title', 'description', 'author__username')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post')
