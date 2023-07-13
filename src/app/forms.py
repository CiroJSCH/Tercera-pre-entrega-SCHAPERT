from django.forms import ModelForm
from django import forms
from .models import Topic, Student, Course


class TopicForm(ModelForm):

    input_text_style = "border-2 border-orange-600 p-2"
    input_textarea_style = "border-2 border-orange-600 p-2 w-full"

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': input_text_style, 'style': 'outline:none'}),
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': input_textarea_style, 'style': 'resize:none; outline:none', 'rows': 5}),
    )

    class Meta:
        model = Topic
        fields = '__all__'


class StudentForm(ModelForm):
    input_text_style = "border-2 border-emerald-600 p-2"

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': input_text_style, 'style': 'outline:none'}),
    )
    surname = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': input_text_style, 'style': 'outline:none'}),
    )

    enrolled_in = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget=forms.SelectMultiple(
            attrs={'class': input_text_style, 'style': 'outline:none'}
        )
    )

    class Meta:
        model = Student
        fields = '__all__'


class CourseForm(ModelForm):
    input_text_style = "border-2 border-blue-600 p-2"
    input_textarea_style = "border-2 border-blue-600 p-2 w-full"

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': input_text_style, 'style': 'outline:none'}),
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': input_textarea_style, 'style': 'resize:none; outline:none', 'rows': 5}),
    )

    category = forms.ModelChoiceField(
        queryset=Topic.objects.all(),
        widget=forms.Select(
            attrs={'class': input_text_style, 'style': 'outline:none'}),
    )

    students = forms.ModelMultipleChoiceField(
        queryset=Student.objects.all(),
        widget=forms.SelectMultiple(
            attrs={'class': input_text_style, 'style': 'outline:none'}
        )
    )

    class Meta:
        model = Course
        fields = '__all__'
