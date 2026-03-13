from django.db import models
from catalog.models import Cake

class Review(models.Model):
    cake_id = models.IntegerField(db_index=True)
    name = models.CharField(max_length=120)
    rating = models.PositiveSmallIntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Отзыв {self.name} - {self.rating}'