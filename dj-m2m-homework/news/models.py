from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Scope(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False)

    class Meta:
        unique_together = ['article', 'tag']

    def __str__(self):
        return f"{self.tag} ({'main' if self.is_main else 'ordinary'})"


class Article(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    published_at = models.DateTimeField()
    image = models.ImageField(null=True, blank=True, upload_to='articles/')

    scopes = models.ManyToManyField(Tag, through=Scope, related_name='articles')

    class Meta:
        ordering = ['-published_at']
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news-detail', args=[self.pk])