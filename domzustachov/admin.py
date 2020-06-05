from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from domzustachov.models import Article
from .models import Author, Composer, Event, Piece, Player

# register models to use in admin site
admin.site.register(Article, MarkdownxModelAdmin)
admin.site.register(Author)
admin.site.register(Event)
admin.site.register(Piece)
admin.site.register(Player)
admin.site.register(Composer)
