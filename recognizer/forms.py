from django import forms

CHOICES = [('query', 'query'),
               ('database', 'database')]

class UploadFileForm(forms.Form):
    video = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    type_of_video = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)