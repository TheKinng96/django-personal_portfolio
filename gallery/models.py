from django.db import models

class Picture(models.Model):
    image = models.ImageField(upload_to = 'gallery/')
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField(max_length=250)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title