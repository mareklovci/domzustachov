import datetime

from django.db import models
from django.utils.text import slugify
from markdownx.models import MarkdownxField
from photologue.models import Photo
from taggit_autosuggest.managers import TaggableManager


class Article(models.Model):
    """Table schema to store articles."""
    title = models.CharField(max_length=64)
    slug = models.SlugField(null=True, blank=True)
    content = MarkdownxField()
    tags = TaggableManager()

    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    # Relationships
    events = models.ManyToManyField('Event', through='ArticleEvent', blank=True)
    composers = models.ManyToManyField('Composer', through='ArticleComposer', blank=True)
    pieces = models.ManyToManyField('Piece', through='ArticlePiece', blank=True)
    players = models.ManyToManyField('Player', through='ArticlePlayer', blank=True)
    photos = models.ManyToManyField('PhotoExtended', through='ArticlePhoto', blank=True)

    def __str__(self):
        return '%s' % self.title

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)

        super(Article, self).save(*args, **kwargs)


class ArticlePhoto(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    photo = models.ForeignKey('PhotoExtended', on_delete=models.CASCADE)

    class Meta:
        db_table = 'domzustachov_article_photo'


class Author(models.Model):
    """Table schema to store authors."""
    name = models.CharField(max_length=64)
    slug = models.SlugField(null=True, blank=True)

    player = models.OneToOneField('Player', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return '%s' % self.name

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.name)

        super(Author, self).save(*args, **kwargs)


class Piece(models.Model):
    """Table schema to store music compositions."""
    name = models.CharField(max_length=64)
    slug = models.SlugField(null=True, blank=True)

    # Relationships
    composers = models.ManyToManyField('Composer', through='ComposerPiece', blank=True)
    events = models.ManyToManyField('Event', through='EventPiece', blank=True)
    articles = models.ManyToManyField('Article', through='ArticlePiece', blank=True)

    def __str__(self):
        return '%s' % self.name

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.name)

        super(Piece, self).save(*args, **kwargs)


class ArticlePiece(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    piece = models.ForeignKey(Piece, on_delete=models.CASCADE)

    class Meta:
        db_table = 'domzustachov_article_piece'


class Composer(models.Model):
    """Table schema to store composers."""
    name = models.CharField(max_length=64)
    slug = models.SlugField(null=True, blank=True)

    # Relationships
    articles = models.ManyToManyField('Article', through='ArticleComposer', blank=True)
    pieces = models.ManyToManyField('Piece', through='ComposerPiece', blank=True)

    def __str__(self):
        return '%s' % self.name

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.name)

        super(Composer, self).save(*args, **kwargs)


class ComposerPiece(models.Model):
    composer = models.ForeignKey(Composer, on_delete=models.CASCADE)
    piece = models.ForeignKey(Piece, on_delete=models.CASCADE)

    class Meta:
        db_table = 'domzustachov_composer_piece'


class ArticleComposer(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    composer = models.ForeignKey(Composer, on_delete=models.CASCADE)

    class Meta:
        db_table = 'domzustachov_article_composer'


class Event(models.Model):
    """Table schema to store events."""
    name = models.CharField(max_length=64)
    slug = models.SlugField(null=True, blank=True)

    # Relationships
    players = models.ManyToManyField('Player', through='EventPlayer', blank=True)
    pieces = models.ManyToManyField('Piece', through='EventPiece', blank=True)
    articles = models.ManyToManyField('Article', through='ArticleEvent', blank=True)
    photos = models.ManyToManyField('PhotoExtended', through='EventPhoto', blank=True)

    def __str__(self):
        return '%s' % self.name

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.name)

        super(Event, self).save(*args, **kwargs)


class EventPhoto(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    photo = models.ForeignKey('PhotoExtended', on_delete=models.CASCADE)

    class Meta:
        db_table = 'domzustachov_event_photo'


class EventPiece(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    piece = models.ForeignKey(Piece, on_delete=models.CASCADE)

    class Meta:
        db_table = 'domzustachov_event_piece'


class ArticleEvent(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    class Meta:
        db_table = 'domzustachov_article_event'


class Player(models.Model):
    """Table schema to store players."""
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    active_from = models.DateField(null=True, blank=True)
    active_to = models.DateField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    # Relationships
    events = models.ManyToManyField('Event', through='EventPlayer', blank=True)
    articles = models.ManyToManyField('Article', through='ArticlePlayer', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(f'{self.first_name} {self.last_name}')

        super(Player, self).save(*args, **kwargs)


class EventPlayer(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    class Meta:
        db_table = 'domzustachov_event_player'


class ArticlePlayer(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    class Meta:
        db_table = 'domzustachov_article_player'


class PhotoExtended(models.Model):
    # Link back to Photologue's Gallery model.
    photo = models.OneToOneField(Photo, related_name='extended', on_delete=models.CASCADE)
    tags = TaggableManager(blank=True)

    articles = models.ManyToManyField('Article', through='ArticlePhoto', blank=True)
    events = models.ManyToManyField('Event', through='EventPhoto', blank=True)

    # Boilerplate code to make a prettier display in the admin interface.
    class Meta:
        verbose_name = u'Extra fields'
        verbose_name_plural = u'Extra fields'

    def __str__(self):
        return self.photo.title
