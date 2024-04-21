from django.db import models


class Destination(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to='images/')

    def _str_(self):
        return self.name

    class Meta:
        app_label = 'myapp'


class Local_news(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    desc = models.TextField()

    def _str_(self):
        return self.name

    class Meta:
        app_label = 'myapp'
