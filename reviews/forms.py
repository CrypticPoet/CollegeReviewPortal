from django import forms
from .models import Prof_review

class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(max_value=10, min_value=1, help_text='Provide a rating')
    body = forms.Textarea()

    class Meta:
        model = Prof_review
        fields = ('rating', 'body')