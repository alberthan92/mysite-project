from django.db import models

# Create your models here.

class Video(models.Model):
    kind = models.CharField(max_length=100)
    youtube_id = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    published_date = models.DateTimeField()
    thumbnail = models.URLField(blank=True)

    def __str__(self):
        return self.title