from django.contrib import admin
from .models import Student, Parent, Class, Subjects, ClassTeacher

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "age"]


class ParentAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


class ClassAdmin(admin.ModelAdmin):
    list_display = ["id", "number", "division"]


class SubjectsAdmin(admin.ModelAdmin):
    list_display = ["name"]


class ClassTeacherAdmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Class)
admin.site.register(ClassTeacher)
admin.site.register(Subjects)
