from django import forms
from .models import Prof_review, Course_review

class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(max_value=10, min_value=1, help_text='Provide a rating')
    anonymous = forms.BooleanField(label='Post Anonymously?', required=False)

    class Meta:
        model = Prof_review
        fields = ['rating', 'body', 'anonymous']

class CourseReviewForm(forms.ModelForm):
    rating = forms.IntegerField(max_value=10, min_value=1, help_text='Provide a rating')
    anonymous = forms.BooleanField(label='Post Anonymously?', required=False)

    class Meta:
        model = Course_review
        fields = ['rating', 'body', 'anonymous']