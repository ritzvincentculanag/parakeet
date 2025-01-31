from django.conf import settings
from django.db import models


class PostModelManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().filter(status=Post.Status.PUBLISHED)
        )
    

class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DFT', 'Draft'
        PUBLISHED = 'PBL', 'Published'

    content = models.CharField(max_length=250)
    likes = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=3,
        choices=Status, 
        default=Status.PUBLISHED
    )
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name='posts',
        on_delete=models.CASCADE
    )

    objects = models.Manager()
    published = PostModelManager()

    def __str__(self):
        return self.content[:50]
    
    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]
