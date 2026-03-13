from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'rating', 'text']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Ваше имя'
            }),
            'rating': forms.NumberInput(attrs={
                'class': 'form-input',
                'min': 1,
                'max': 5,
                'placeholder': 'Оценка от 1 до 5'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-input',
                'rows': 5,
                'placeholder': 'Напишите ваш отзыв'
            }),
        }