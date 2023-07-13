from django.db import models

# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)


class Student(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    enrolled_in = models.ManyToManyField('Course', blank=True)


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Topic, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, blank=True)
