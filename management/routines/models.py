from django.db import models


class Exercise(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __unicode__(self):
        return self.name
