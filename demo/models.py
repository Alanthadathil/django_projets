from django.db import models

# Create your models here.


class Student(models.Model):
    register_id = models.IntegerField(primary_key=True)
    age = models.IntegerField()
    name = models.CharField(max_length=255)
    rollnum = models.IntegerField()
    _class = models.IntegerField()
    parent = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self) -> str:
        return super().__str__()


class Parent(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    occupation = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Parent"
        verbose_name_plural = "Parents"

    def __str__(self) -> str:
        return super().__str__()


class Class(models.Model):
    id = models.IntegerField(primary_key=True)
    number = models.IntegerField()
    division = models.CharField(max_length=255)
    class_teacher = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Class"

    def __str__(self) -> str:
        return super().__str__()


class Subjects(models.Model):
    name = models.CharField(max_length=255)
    hours_per_week = models.FloatField()

    class Meta:
        verbose_name = "Subjects"
        verbose_name_plural = "Subjects"

    def __str__(self) -> str:
        return super().__str__()


class ClassTeacher(models.Model):
    phone_number = models.IntegerField()
    name = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    subject_handled = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Class Teacher"
        verbose_name_plural = "Class Teachers"

    def __str__(self) -> str:
        return super().__str__()
