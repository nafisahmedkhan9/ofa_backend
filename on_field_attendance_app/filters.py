from django.db import models as django_models
import django_filters
from rest_framework import filters
from rest_framework import viewsets
from .models import *

class TaskFilters(django_filters.FilterSet):
	class Meta:
		model = Task
		fields = {
			"assignedTo" : ["exact"],
			"title": ["exact"],
            "comment": ["exact"],
            "date": ["exact"],
			"status": ["exact"],
		}

class AttendanceFilters(django_filters.FilterSet):
	class Meta:
		model = Attendance
		fields = {
			"task" : ["exact"],
			"employee" : ["exact"],
			"date" : ["exact"],
			"attendance" : ["exact"],
		}

class EmployeeFilters(django_filters.FilterSet):
    class Meta:
        model = Employee
        fields = {
			"designation" : ["exact"],
			"username": ["exact"],
            "first_name": ["exact"],
            "last_name": ["exact"],
            "city": ["exact"],
            "state": ["exact"],
            "mobile_no":["exact"],
            "email": ["exact"],
            "designation": ["exact"],
		}