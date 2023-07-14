from django.forms import ModelForm
from django import forms
from .models import Topic, Student, Course


class TopicForm(ModelForm):

    class Meta:
        model = Topic
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': "border-2 border-orange-600 p-2", 'style': 'outline:none'}),
            'description': forms.Textarea(attrs={'class': "border-2 border-orange-600 p-2 w-full", 'style': 'resize:none; outline:none', 'rows': 5}),
        }


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'surname')
        widgets = {
            'name': forms.TextInput(attrs={'class': "border-2 border-emerald-600 p-2", 'style': 'outline:none'}),
            'surname': forms.TextInput(attrs={'class': "border-2 border-emerald-600 p-2", 'style': 'outline:none'}),
        }


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'description', 'category', 'students')
        widgets = {
            'name': forms.TextInput(attrs={'class': "border-2 border-blue-600 p-2", 'style': 'outline:none'}),
            'description': forms.Textarea(attrs={'class': "border-2 border-blue-600 p-2 w-full", 'style': 'resize:none; outline:none', 'rows': 5}),
            'category': forms.Select(attrs={'class': "border-2 border-blue-600 p-2", 'style': 'outline:none'}),
            'students': forms.SelectMultiple(attrs={'class': "border-2 border-blue-600 p-2", 'style': 'outline:none'}),
        }
