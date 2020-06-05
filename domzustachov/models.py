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
    events = models.ManyToManyField('Event', through='ArticleEvent', blank=True)
    composers = models.ManyToManyField('Composer', through='ArticleComposer', blank=True)
    pieces = models.ManyToManyField('Piece', through='ArticlePiece', blank=True)
    players = models.ManyToManyField('Player', through='ArticlePlayer', blank=True)

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
    slug = models.SlugField(null=True, blank=True)

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
    composers = models.ManyToManyField('Composer', blank=True)
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
    pieces = models.ManyToManyField('Piece', through=Piece.composers.through, blank=True)

    def __str__(self):
        return '%s' % self.name

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.name)

        super(Composer, self).save(*args, **kwargs)


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

    def __str__(self):
        return '%s' % self.name

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.name)

        super(Event, self).save(*args, **kwargs)


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
    slug = models.SlugField(null=True, blank=True)

    # Relationships
    events = models.ManyToManyField('Event', through='EventPlayer', blank=True)
    articles = models.ManyToManyField('Article', through='ArticlePlayer', blank=True)

    def __str__(self):
        return '%s' % self.first_name

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
