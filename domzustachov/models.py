from django.db import models
from django.utils.text import slugify
from markdownx.models import MarkdownxField


class Article(models.Model):
    """Table schema to store articles."""
    title = models.CharField(max_length=64)
    slug = models.SlugField(null=True, blank=True)
    content = MarkdownxField()

    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    # Relationships
    events = models.ManyToManyField('Event', blank=True)
    composers = models.ManyToManyField('Composer', blank=True)
    pieces = models.ManyToManyField('Piece', blank=True)
    players = models.ManyToManyField('Player', blank=True)

    def __str__(self):
        return '%s' % self.title

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)

        super(Article, self).save(*args, **kwargs)


class Author(models.Model):
    """Table schema to store authors."""
    name = models.CharField(max_length=64)
    slug = models.CharField(default='', max_length=64)

    def __str__(self):
        return '%s' % self.name


class Piece(models.Model):
    """Table schema to store music compositions."""
    name = models.CharField(max_length=64)
    slug = models.CharField(default='', max_length=64)

    # Relationships
    composers = models.ManyToManyField('Composer', blank=True)
    events = models.ManyToManyField('Event', blank=True)
    articles = models.ManyToManyField('Article', through=Article.pieces.through, blank=True)

    def __str__(self):
        return '%s' % self.name


class Composer(models.Model):
    """Table schema to store composers."""
    name = models.CharField(max_length=64)
    slug = models.CharField(default='', max_length=64)

    # Relationships
    articles = models.ManyToManyField('Article', through=Article.composers.through, blank=True)
    pieces = models.ManyToManyField('Piece', through=Piece.composers.through, blank=True)

    def __str__(self):
        return '%s' % self.name


class Event(models.Model):
    """Table schema to store events."""
    name = models.CharField(max_length=64)
    slug = models.CharField(default='', max_length=64)

    # Relationships
    players = models.ManyToManyField('Player')
    pieces = models.ManyToManyField('Piece', through=Piece.events.through, blank=True)
    articles = models.ManyToManyField('Article', through=Article.events.through, blank=True)

    def __str__(self):
        return '%s' % self.name


class Player(models.Model):
    """Table schema to store players."""
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    slug = models.CharField(default='', max_length=64)

    # Relationships
    events = models.ManyToManyField('Event', through=Event.players.through, blank=True)
    articles = models.ManyToManyField('Article', through=Article.players.through, blank=True)

    def __str__(self):
        return '%s' % self.first_name
