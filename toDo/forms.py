from django import forms

from .models import toDo

"""
class toDoForm(forms.ModelForm):
    class Meta:
        
        model = toDo
        fields = ('text', 'description',)

        widgets = {
            'text': forms.TextInput(attrs = {'class':'form-control'}),
            'added_date': forms.TextInput(attrs = {'class':'form-control'}),
            'description': forms.Textarea(attrs = {'class':'form-control'})
        }
"""
class toDoForm(forms.Form):
    Todo = forms.CharField(widget= forms.TextInput(attrs = {'class':"form-control"}))
    Date = forms.DateTimeField(widget= forms.TextInput(attrs = {'class': "form-control" }))
    Description = forms.CharField(required = False, widget = forms.Textarea(attrs = {'class':"form-control", 'placeholder':"Describe your toDo!"}))
