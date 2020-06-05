from django.contrib import admin
from markdownx.admin import AdminMarkdownxWidget
from markdownx.models import MarkdownxField

from domzustachov.models import Article
from .models import ArticleComposer, ArticleEvent, ArticlePiece, ArticlePlayer, Author, Composer, Event, Piece, Player


class ArticlePieceInline(admin.TabularInline):
    model = ArticlePiece
    extra = 1


class ArticleComposerInline(admin.TabularInline):
    model = ArticleComposer
    extra = 1


class ArticleEventInline(admin.TabularInline):
    model = ArticleEvent
    extra = 1


class ArticlePlayerInline(admin.TabularInline):
    model = ArticlePlayer
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    inlines = (
        ArticlePieceInline,
        ArticleComposerInline,
        ArticleEventInline,
        ArticlePlayerInline,
    )
    formfield_overrides = {
        MarkdownxField: {'widget': AdminMarkdownxWidget}
    }


class PieceAdmin(admin.ModelAdmin):
    inlines = (ArticlePieceInline,)


class ComposerAdmin(admin.ModelAdmin):
    inlines = (ArticleComposerInline,)


class EventAdmin(admin.ModelAdmin):
    inlines = (ArticleEventInline,)


class PlayerAdmin(admin.ModelAdmin):
    inlines = (ArticlePlayerInline,)


# register models to use in admin site
admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
admin.site.register(Event, EventAdmin)
admin.site.register(Piece, PieceAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Composer, ComposerAdmin)
