from django.db import models
from django.db.models import Model


class Customer(Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Customer'

    def  __str__(self):
        return f"{self.name} {self.last_name}, {self.address}"


