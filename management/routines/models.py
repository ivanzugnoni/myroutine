from django.db import models
import random, string

MUSCLE_GROUP_CHOICES = (
    ('pecho', 'Pecho'),
    ('espalda', 'Espalda'),
    ('biceps', 'Biceps'),
)

def get_hash_id():
    """Generates random 16 char lowercase string with numbers and letters"""
    hash_seed = string.ascii_lowercase + string.digits
    hash_string = ''
    for x in random.sample(hash_seed, 16):
        hash_string += x
    return hash_string


class Exercise(models.Model):

    id = models.CharField(primary_key=True, default=get_hash_id, max_length=16,
                          editable=False)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    muscle_group = models.CharField(max_length=100,
                                    choices=MUSCLE_GROUP_CHOICES)

    def __unicode__(self):
        return self.name


