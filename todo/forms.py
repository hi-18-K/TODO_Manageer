from django import forms
from django.forms import ModelForm
from datetime import datetime, timedelta, tzinfo
from . models import Todo

# class DateInput(forms.DateTimeInput):
#     input_type='datetime'

class TodoForm(forms.Form):
    text = forms.CharField(max_length=200,
        widget=forms.TextInput(
            attrs={'class' : 'column form-control', 'placeholder' : 'add task', 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn'}))

    priority = forms.CharField(max_length=8,
        widget=forms.TextInput(

            attrs={'class' : 'column form-control', 'placeholder' : 'Enter priority' , 'aria-describedby' : 'add-btn'}))

    type = forms.CharField(max_length=20,
        widget=forms.TextInput(
            attrs={'class' : 'column form-control', 'placeholder' : 'type:-school/home..' , 'aria-describedby' : 'add-btn'}))

    duedate = forms.DateTimeField(widget= DateInput)
    #duedate = forms.DateTimeField(widget=forms.DateTimeInput(attrs={ 'aria-describedby' : 'add-btn' , 'type' : 'datetime-local'}))
    #duetime = forms.DateTimeField(widget=DateTimeInput)
#
# class TodoForm(forms.ModelForm):
#     class Meta:
#         model = Todo
#         fields = ['text' , 'priority' , 'type' , 'duedate' ]
