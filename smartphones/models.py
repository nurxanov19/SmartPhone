from django.db import models
from django.db.models import Model



class SmartPhone(Model):
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    year = models.PositiveIntegerField(blank=True, null=True)   # blank = True --> qiymat kiritilmasa ham bo'ladi, null = True --> qiymat kiritilmasa null oladi yoiki default = 0
    color = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='phone_image/', blank=True, null=False)       # upload_to >> qaysi adresga yuklashini belgilash


    class Meta:
        ordering = ['-created_at']      # ordering berilgan argument bo'yicha tartiblaydi

        verbose_name = 'SmartPhone'

    def __str__(self):
        return f"{self.brand} {self.model} ({self.color})"

