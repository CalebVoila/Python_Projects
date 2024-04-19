from django.db import models


class Destination(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

    def _str_(self):
        return self.name

    class Meta:
        app_label = 'myapp'
