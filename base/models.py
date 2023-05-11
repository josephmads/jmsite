from django.db import models

# Create your models here.

class PageElement(models.Model):
    """Model class to create editable page elements."""
    title = models.CharField(max_length=140)
    content = models.TextField()

    def __str__(self):
        return self.title