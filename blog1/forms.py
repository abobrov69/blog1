from django import forms
from models import Publication

#class MsgTextArea (forms.Textarea)

class MsgForm(forms.Form):
    wj = forms.Textarea(attrs={'cols': 80, 'rows': 3, 'class': "span9"})
    message = forms.CharField(widget=wj , max_length=140, label='Input text of new message here')
    errmsg = ''
    user = ''

    def as_p(self):
        "Returns this form rendered as HTML <p>s."
        if len(self.errors)>0:
            self.errmsg = self.errors[next(iter(self.errors))][0] #    ee = e['message'][0]
#        elif: self.errmsg = ''
        out = self._html_output(
            normal_row = '<p%(html_class_attr)s>%(label)s %(field)s%(help_text)s</p>',
            error_row = '%s',
            row_ender = '</p>',
            help_text_html = ' <span class="helptext">%s</span>',
            errors_on_separate_row = False)
#        aa = aawerwer
        return out

class MsgForm2 (forms.ModelForm):
    class Meta:
        model = Publication
        exclude = ('date','author','isdeleted')
#        fields = ('text')
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 3, 'class': "span9"}),
        }