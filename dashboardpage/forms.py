from django import forms
from .models import TaskUsers,Projects
class TaskForm(forms.Form):
    title=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    description=forms.CharField(max_length=300,widget=forms.Textarea(attrs={"class":"form-control"}))
    dead_line=forms.DateField(widget=forms.DateInput(attrs={"type":"date","placeholder":"yyyy-mm-dd","class":"form-control"}))

choice={}
class ProjectForm(forms.Form):
    title=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    tasks=forms.ModelMultipleChoiceField(queryset=TaskUsers.objects.all(),widget=forms.SelectMultiple(attrs={"class":"form-control"}))
    dead_line=forms.DateField(widget=forms.DateInput(attrs={"type":"date","placeholder":"yyyy-mm-dd","class":"form-control"}))

class AlarmTaskForm(forms.Form):
    alarm_d=forms.DateField(widget=forms.DateInput(attrs={"type":"date","placeholder":"yyyy-mm-dd","class":"form-control"}))
    alarm_t=forms.TimeField(widget=forms.TimeInput(attrs={"class":"form-control","type":"time"}))