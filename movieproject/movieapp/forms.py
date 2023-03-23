from django import forms #we need to import forms
from . models import Movie #we need to import movie table because here only we can update the details


#here we need to create model for our form
class MovieForm(forms.ModelForm):
    class Meta: #meta class is used to render the fields in table
        model = Movie #mention here the table name u need to edit
        fields = ['name','desc','year','img'] #mention the fields we need to edit
