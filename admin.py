from django.contrib import admin
from .models import Student, Job, Application


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "course", "cgpa")


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "company",
        "location",
        "salary",
        "required_cgpa",
        "last_date"
    )


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "job",
        "applied_date",
        "status"
    )