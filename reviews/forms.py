from django import forms

class ReviewForm(forms.Form):
  user_name = forms.CharField(label="User Name",required=True, max_length=50, error_messages={
    "required": "Please enter your name"
  })
  review_text = forms.CharField(label="Feedback",widget=forms.Textarea, max_length=200 )
  rating = forms.IntegerField(label="Rating", min_value=1, max_value=5)
 

