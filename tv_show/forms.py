from django import forms
from . import models


class MovieForm(forms.ModelForm):
    class Meta:
        model = models.Movie
        fields = "__all__"


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = [
            'comment',
            'rating',
        ]
