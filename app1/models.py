# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=50)
    course_duration = models.TextField()
    time = models.TimeField(auto_now=False, auto_now_add=False)
    fee = models.IntegerField()


    def __str__(self):
        return self.name


class Student(models.Model):
    course = models.ManyToManyField(Course)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    qualification = models.CharField(max_length=15)
    mobile = models.CharField(max_length=15, blank=True, default=None)
    batch = models.CharField(max_length=30, blank=True, default=None)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Staff(models.Model):
    name = models.CharField(max_length=100)
    exp = models.CharField(max_length=10, blank=True, default=None)
    salary = models.IntegerField()
    course = models.ManyToManyField(Course)

    def __str__(self):
        return self.name
