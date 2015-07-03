from django.db import models

MUSCLE_GROUP_CHOICES = (
    ('pecho', 'Pecho'),
    ('espalda', 'Espalda'),
    ('biceps', 'Biceps'),
)


class Exercise(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    muscle_group = models.CharField(max_length=100,
                                    choices=MUSCLE_GROUP_CHOICES)

    def __unicode__(self):
        return self.name
