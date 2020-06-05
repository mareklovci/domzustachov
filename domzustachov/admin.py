from django.contrib import admin
from markdownx.admin import AdminMarkdownxWidget
from markdownx.models import MarkdownxField

from domzustachov.models import Article
from .models import ArticlePiece, Author, Composer, Event, Piece, Player


class ArticlePieceInline(admin.TabularInline):
    model = ArticlePiece
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    inlines = (ArticlePieceInline,)
    formfield_overrides = {
        MarkdownxField: {'widget': AdminMarkdownxWidget}
    }


class PieceAdmin(admin.ModelAdmin):
    inlines = (ArticlePieceInline,)


# register models to use in admin site
admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
admin.site.register(Event)
admin.site.register(Piece, PieceAdmin)
admin.site.register(Player)
admin.site.register(Composer)
