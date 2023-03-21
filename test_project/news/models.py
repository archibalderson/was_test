from django.db import models


class News(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    date = models.CharField(max_length=12)
    text = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.title + self.author + self.date + self.text
