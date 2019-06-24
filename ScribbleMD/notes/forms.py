from django import forms


class NewNote(forms.Form):
    heading = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
