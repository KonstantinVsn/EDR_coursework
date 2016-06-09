from django import forms

class SearchForm(forms.Form):
    input = forms.CharField(max_length=200, required=False)


