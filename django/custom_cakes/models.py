from django.db import models

class CustomCakeRequest(models.Model):
    customer_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    description = models.TextField()
    event_date = models.DateField(blank=True, null=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f'Заявка #{self.id} - {self.customer_name}'
