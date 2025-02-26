from django.db import models
from django.db.models import Model
from smartphones.models import SmartPhone
from users.models import Customer

class Orders(Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(SmartPhone, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Orders'

    def __str__(self):
        return f"{self.user} -- {self.product}"


