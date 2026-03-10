from django.db import models
from catalog.models import Cake

class Review(models.Model):
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=120)
    rating = models.PositiveSmallIntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Отзыв {self.name} - {self.cake.name}'