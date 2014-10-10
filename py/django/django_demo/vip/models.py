from django.db import models
from django.contrib.auth.models import User


class VIPUser(models.Model):
    
    user = models.ForeignKey(User, unique=True)
    phone = models.CharField(max_length=11, default='00000000000')
    balance = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    scores = models.PositiveIntegerField(default=0)
    
    
    def __str__(self):
        return '{0}({1})'.format(self.user.username, self.user.id)
