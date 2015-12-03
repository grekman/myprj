from django.contrib import admin

# Register your models here.
from blog.models import Category, Tag, Article
from django import forms
from django.conf import settings
from redactor.widgets import RedactorEditor

# admin.site.register(Category)
# admin.site.register(Tag)
#admin.site.register(Article)

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('views_count',)
    list_display = ('name', 'slug')
    list_display_links = ('name',)
    search_fields = ['name', 'slug', 'description']
    list_per_page = settings.ADMIN_LIST_PER_PAGE
#    fields = ('name', 'slug', 'description')
    prepopulated_fields = {"slug": ("name",)}
#    readonly_fields = ("slug",)

admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag)

def make_published(modeladmin, request, queryset):
    queryset.update(status = PUBLISHED)
make_published.short_description = "Mark selected stories as published"

class ArticleAdminForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'content': RedactorEditor(),
        }


# class ArticleAdmin(admin.ModelAdmin):
#    fields = ['title','category','content','created_date','publish_date','tags','status','enable_comment','views_count','comment_count']

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date', 'status', 'was_published_recently')
    list_filter = ['publish_date']
    search_fields = ['title']
    fieldsets = [
        ('Item',             {'fields': ['title','slug','category','content']}),
        ('Date information', {'fields': ['created_date','publish_date'], 'classes': ['collapse']}),
        ('Related tags',     {'fields': ['tags']}),
        ('Metas',            {'fields': ['status','views_count']}),
        ('Comments',            {'fields': ['enable_comment','comment_count']}),
    ]
    actions = [make_published,'make_draft','make_expired']
    form = ArticleAdminForm

admin.site.register(Article, ArticleAdmin)
