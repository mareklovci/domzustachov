from django.contrib import admin
from markdownx.admin import AdminMarkdownxWidget
from markdownx.models import MarkdownxField

from domzustachov.models import Article
from .models import ArticleComposer, ArticlePiece, Author, Composer, Event, Piece, Player


class ArticlePieceInline(admin.TabularInline):
    model = ArticlePiece
    extra = 1


class ArticleComposerInline(admin.TabularInline):
    model = ArticleComposer
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    inlines = (
        ArticlePieceInline,
        ArticleComposerInline,
    )
    formfield_overrides = {
        MarkdownxField: {'widget': AdminMarkdownxWidget}
    }


class PieceAdmin(admin.ModelAdmin):
    inlines = (ArticlePieceInline,)


class ComposerAdmin(admin.ModelAdmin):
    inlines = (ArticleComposerInline,)


# register models to use in admin site
admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
admin.site.register(Event)
admin.site.register(Piece, PieceAdmin)
admin.site.register(Player)
admin.site.register(Composer, ComposerAdmin)
