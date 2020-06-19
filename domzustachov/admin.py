from django.contrib import admin
from django.utils.safestring import mark_safe
from markdownx.admin import AdminMarkdownxWidget
from markdownx.models import MarkdownxField
from photologue.admin import PhotoAdmin as PhotoAdminDefault
from photologue.models import Photo

from .models import Article, ArticleComposer, ArticleEvent, ArticlePhoto, ArticlePiece, ArticlePlayer, Author, \
    Composer, ComposerPiece, Event, EventPiece, EventPlayer, PhotoExtended, Piece, Player, EventPhoto


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


class ArticlePhotoInline(admin.TabularInline):
    model = ArticlePhoto
    extra = 1

    readonly_fields = ('render_image',)

    @staticmethod
    def render_image(obj):
        return mark_safe(f'<img src="{obj.photo.photo.get_admin_thumbnail_url()}" />')


class EventPhotoInline(admin.TabularInline):
    model = EventPhoto
    extra = 1

    readonly_fields = ('render_image',)

    @staticmethod
    def render_image(obj):
        return mark_safe(f'<img src="{obj.photo.photo.get_admin_thumbnail_url()}" />')


class ArticleAdmin(admin.ModelAdmin):
    inlines = (
        ArticlePieceInline,
        ArticleComposerInline,
        ArticleEventInline,
        ArticlePlayerInline,
        ArticlePhotoInline,
    )
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
        EventPhotoInline,
    )


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'active_from', 'active_to')
    inlines = (
        ArticlePlayerInline,
        EventPlayerInline,
    )


class PhotoExtendedInline(admin.StackedInline):
    model = PhotoExtended
    can_delete = False


class PhotoAdmin(PhotoAdminDefault):
    inlines = (PhotoExtendedInline,)
    exclude = ('articles', 'events',)


admin.site.unregister(Photo)
admin.site.register(Photo, PhotoAdmin)

# register models to use in admin site
admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
admin.site.register(Event, EventAdmin)
admin.site.register(Piece, PieceAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Composer, ComposerAdmin)
