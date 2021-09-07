from django.db import models

# Create your models here.
class Subject(models.Model):
    SUBJECT_NAME = (
        ('ENG','English'),
        ('ENGl', 'English Lit'),
        ('KISW', 'Kiswahili'),
        ('KISW1', 'Kiswahili Fasihi'),
        ('MATH', 'Mathematics'),
        ('Bio', 'Biology'),
        ('CHEM', 'Chemistry'),
        ('Geo', 'Geography'),
        ('HIS', 'History'),
        ('CRE', 'Christian Religious Education'),
        ('Agr', 'Agriculture'),
    )
    name = models.CharField(max_length=5, choices=SUBJECT_NAME, default='ENG')
    CATEGORY = (
        ('s', 'Sciences'),
        ('L', 'Languages'),
        ('T', 'Technicals'),
        ('A', 'Arts'),
        ('B', 'Business'),

    )
    category =models.CharField(max_length=5, choices=CATEGORY, default='L')

    def __str__(self):
        return f'{self.name}, {self.category}'

class TeacherRole(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)

    def __str__(self):
        return f'{self.name}, {self.description}'


class Teacher(models.Model):
    TSC_Number = models.CharField(max_length=100, unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    GENDER= (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    gender = models.CharField(max_length=100, choices=GENDER, default='F')
    date_of_birth = models.DateField()
    subject = models.ManyToManyField('Subject', blank=True)

    def __str__(self):
        return f'{self.name}, {self.TSC_Number}'

class Assign_Role(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    Role = models.ManyToManyField(TeacherRole, blank=True)
    StartDate = models.DateField()
    Duration = models.IntegerField()

    def __str__(self):
        return f'{self.Role}, {self.StartDate}'
class StudentRole(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'
