from django import forms
from ecoeats.models import Feedback

class FeedbackForm(forms.ModelForm):
    feedback = forms.CharField(max_length=1000, help_text="Please enter your feedback here.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
   # slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Feedback
        fields = ('feedback',)