from django import forms
from models import Publication

class MsgForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, max_length=140)

class MsgForm2 (forms.ModelForm):
    class Meta:
        model = Publication
        exclude = ('date',)