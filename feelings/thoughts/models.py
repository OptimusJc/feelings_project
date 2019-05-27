from django.contrib.auth.models import User #import  user
from django.db import models
from django.utils import timezone

CONDITIONS = {
    (1, 'Joy'),
    (2, 'Passionate'),
    (3, 'Frustrated'),
    (4, 'Optimistic'),
    (5, 'Content'),
    (6, 'Bored'),
    (7, 'Pessimistic'),
    (8, 'Doubt'),
    (9, 'Worried'),
    (10, 'Jealous'),
    (11, 'Fear'),
    (12, 'Hungry'),
    (13, 'Tired'),
    (14, 'Paranoia'),
    (15, 'Disappointed')
}


class Thought(models.Model):
    user = models.ForeignKey(User, related_name='thoughts', on_delete=models.CASCADE)
    recorded_at = models.DateTimeField(default=timezone.now)
    condition = models.IntegerField(choices=CONDITIONS)
    notes = models.TextField(blank=True, default="")

    def __str__(self):
        return '{}: {}'.format(self.recorded_at.strftime('%Y-%m-%d %H:%M:%S'), self.condition)

