from django.db import models
from django.contrib.auth.models import User


BLUETOOTH_ADDR_DEFAULT = '00:00:00:00:00:00'
BLUETOOTH_ADDR_LEN = len(BLUETOOTH_ADDR_DEFAULT)


class VIPUser(models.Model):
    
    user = models.ForeignKey(User, unique=True)
    phone = models.CharField(max_length=11, default='00000000000')
    bluetooth_addr = models.CharField(max_length=BLUETOOTH_ADDR_LEN,
            default=BLUETOOTH_ADDR_DEFAULT)
    balance = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    scores = models.PositiveIntegerField(default=0)
    
    
    def __str__(self):
        return '{0}({1})'.format(self.user.username, self.user.id)
        
        
class Bill(models.Model):
    user = models.ForeignKey(VIPUser)
    item = models.CharField(max_length=128)
    num = models.PositiveIntegerField(default=1)
    unit = models.CharField(max_length=16)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    total = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    date = models.DateTimeField()
    
    
    def __str__(self):
        return '{0}: {1}'.format(self.user, self.date)
