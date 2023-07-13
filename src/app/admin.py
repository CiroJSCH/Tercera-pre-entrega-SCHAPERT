from django.contrib import admin
from .models import Topic, Student, Course
# Register your models here.

admin.site.register(Student)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'students_count')

    def students_count(self, obj):
        return obj.student_set.count()

    students_count.short_description = 'Students Count'


class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'courses_count')

    def courses_count(self, obj):
        return obj.course_set.count()

    courses_count.short_description = 'Courses Count'


admin.site.register(Course, CourseAdmin)
admin.site.register(Topic, TopicAdmin)
