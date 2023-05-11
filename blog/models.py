from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=140)
    slug = models.SlugField(max_length=140, default='', null=True, blank=True, unique=True)
    text = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(to=Tag, related_name="posts", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

        