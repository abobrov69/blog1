from django import forms

class MsgForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, max_length=140)