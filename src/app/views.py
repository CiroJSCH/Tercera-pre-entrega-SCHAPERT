from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import TopicForm, StudentForm, CourseForm
from .models import Topic, Student, Course

# Create your views here.


def index(request):
    topic_form = TopicForm()
    student_form = StudentForm()
    course_form = CourseForm()

    topics = Topic.objects.all()
    courses = Course.objects.all()

    if request.path == "/create_topic/":
        topic_form = TopicForm(request.POST)
        if topic_form.is_valid():
            topic_form.save()
            return redirect("index")

    if request.path == "/create_student/":
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save()
            return redirect("index")

    if request.path == "/create_course/":
        course_form = CourseForm(request.POST)
        if course_form.is_valid():
            course = course_form.save(commit=False)
            students = course_form.cleaned_data['students']

            course.save()

            for student in students:
                student.enrolled_in.add(course)
                student.save()

            return redirect("index")

    search_query = request.GET.get('student-name')

    if search_query:
        search_students = Student.objects.filter(
            Q(name__istartswith=search_query) | Q(
                surname__istartswith=search_query)
        )
    else:
        search_students = Student.objects.all()

    course_id = request.GET.get('courses')
    filter_students = Student.objects.filter(
        enrolled_in__id=course_id) if course_id and course_id != 'all' else Student.objects.all()

    return render(request, 'main.html', {'topic_form': topic_form, 'student_form': student_form, 'course_form': course_form, 'topics': topics, 'courses': courses, 'search_students': search_students, 'filter_students': filter_students})
