from django.db import models
from django.conf import settings
from django.utils import timezone


class BuzzPublishedManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().filter(status=Buzz.Status.PUBLISHED)
        )


class Buzz(models.Model):
    class Status(models.TextChoices):
        PUBLISHED = 'PBL', 'Published'
        DRAFT = 'DFT', 'Draft'

    title = models.CharField(max_length=250)
    body = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='buzzes'
    )
    status = models.CharField(
        max_length=3,
        choices=Status,
        default=Status.DRAFT
    )

    published = BuzzPublishedManager()
    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'Buzzes'
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self):
        return self.title
