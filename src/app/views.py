from django.shortcuts import render
from .forms import TopicForm, StudentForm, CourseForm
from .models import Topic, Student, Course

# Create your views here.


def index(request):
    topic_form = TopicForm()
    student_form = StudentForm()
    course_form = CourseForm()

    topics = Topic.objects.all()
    courses = Course.objects.all()
    students = Student.objects.all()

    return render(request, 'main.html', {'topic_form': topic_form, 'student_form': student_form, 'course_form': course_form, 'topics': topics, 'courses': courses, 'students': students})
