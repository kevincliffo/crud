from django import forms
from . import models

class AddTask(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ['name','description','date_added', 'finished', 'slug']
        labels = {
            'name':'Name','description':'Description','date_added':'Date Added', 'finished':'Finished', 'slug':'Slug'
        }
        widgets = {
            'finished' : forms.CheckboxInput(attrs={'class': 'finished-cb', 'id':'id_finished', 'name':'finished'})
        }        
            