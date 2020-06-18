from django.contrib import admin
from markdownx.admin import AdminMarkdownxWidget
from markdownx.models import MarkdownxField
from django.utils.safestring import mark_safe

from .models import Article, ArticleComposer, ArticleEvent, ArticlePiece, ArticlePlayer, Author, Composer, \
    ComposerPiece, Event, EventPiece, EventPlayer, Image, Piece, Player


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


class ComposerPieceInline(admin.TabularInline):
    model = ComposerPiece
    extra = 1


class EventPlayerInline(admin.TabularInline):
    model = EventPlayer
    extra = 1


class EventPieceInline(admin.TabularInline):
    model = EventPiece
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    inlines = (
        ArticlePieceInline,
        ArticleComposerInline,
        ArticleEventInline,
        ArticlePlayerInline,
    )
    filter_horizontal = ('images',)
    formfield_overrides = {
        MarkdownxField: {'widget': AdminMarkdownxWidget}
    }


class PieceAdmin(admin.ModelAdmin):
    inlines = (
        ArticlePieceInline,
        EventPieceInline,
        ComposerPieceInline,
    )


class ComposerAdmin(admin.ModelAdmin):
    inlines = (
        ArticleComposerInline,
        ComposerPieceInline,
    )


class EventAdmin(admin.ModelAdmin):
    inlines = (
        ArticleEventInline,
        EventPlayerInline,
        EventPlayerInline,
    )


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'active_from', 'active_to')
    inlines = (
        ArticlePlayerInline,
        EventPlayerInline,
    )


# register models to use in admin site
admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
admin.site.register(Event, EventAdmin)
admin.site.register(Piece, PieceAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Composer, ComposerAdmin)
admin.site.register(Image)
