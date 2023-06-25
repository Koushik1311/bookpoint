from django.db import models


class EbookModel(models.Model):
    name = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=250, null=True)
    category = models.CharField(max_length=200, default='Uncategorized')
    price = models.FloatField()
    digital = models.BooleanField(default=True)
    image = models.ImageField(null=True, blank=True)
    file = models.FileField(null=True, blank=True)
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url