from django.db import models

from django.db import models

class Movies(models.Model):
    title = models.CharField(max_length=100, null=False)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField(null=False, default="Something")
    download_link = models.URLField(max_length=200, blank=True, null=True)  # Field for the download link
    thumbnail_video_link = models.URLField(max_length=200, blank=True, null=True)  # Field for the thumbnail video link

    def __str__(self):
        return self.title

    
class Categories(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title