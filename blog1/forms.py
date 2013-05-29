from django import forms
from models import Publication

#class MsgTextArea (forms.Textarea)

class MsgForm(forms.Form):
    wj = forms.Textarea(attrs={'cols': 80, 'rows': 3, 'class': "span10"})
    message = forms.CharField(widget=wj , max_length=140, label='Input text of new message here')

    def as_p(self):
        "Returns this form rendered as HTML <p>s."
        return self._html_output(
            normal_row = '<p%(html_class_attr)s>%(label)s %(field)s%(help_text)s</p>',
            error_row = '%s',
            row_ender = '</p>',
            help_text_html = ' <span class="helptext">%s</span>',
            errors_on_separate_row = False)

class MsgForm2 (forms.ModelForm):
    class Meta:
        model = Publication
        exclude = ('date',)
#        fields = ('text')
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }