from django.contrib import admin
from .models import Comment, PostModel

class PostModelAdmin(admin.ModelAdmin):
    model = PostModel
    list_display = ["autore",]
    search_fields = ["contenuto"]
    list_filter = ["data_creazione", "autore"]

class CommentAdmin(admin.ModelAdmin):
    list_display = ['post','data','active']
    search_fields = ['post', 'contenuto_commento','data']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(PostModel, PostModelAdmin)
admin.site.register(Comment, CommentAdmin)
