from django.contrib import admin
from .models import Post, Comment, Submit_Recipe
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Submit_Recipe)
class Submit_RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'ingredients', 'instructions', 'created_on', 'status', )
    list_filter = ('status', 'created_on')
    search_fields = ('author', 'email', 'body')
    actions = ['approve_recipes']

    def approve_recipes(modeladmin, request, queryset):
        queryset.update(approved=True)

    approve_recipes.short_description = "Approve selected recipes"
