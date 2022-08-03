from dataclasses import field
from django import forms

from reviews.models import Review

# class ReviewForm(forms.Form):
#   user_name = forms.CharField(label="User Name",required=True, max_length=50, error_messages={
#     "required": "Please enter your name"
#   })
#   review_text = forms.CharField(label="Feedback",widget=forms.Textarea, max_length=200 )
#   rating = forms.IntegerField(label="Rating", min_value=1, max_value=5)
 
class ReviewForm(forms.ModelForm):
  class Meta:
    model = Review
    fields = '__all__'
    labels = {
            "user_name": "User Name",
            "review_text": "Feedback",
            "rating": "Rating"
        }
    error_messages = {
            "user_name": {
              "required": "Your name must not be empty!",
              "max_length": "Please enter a shorter name!"
            }
        }
