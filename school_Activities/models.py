from django.db import models
from student.models import Class_Room, Student_Admission
from teachers.models import  Teacher
from transport.models import Bus
# Create your models here.
class School_Activity(models.Model):
    ACTIVITYTYPE= (
        ('AC', 'Academic Activity'),
        ('GS', 'Games & Sports'),
        ('Cl', 'Clubs Activity'),
        ('OT', 'Other Activity'),
    )
    type = models.CharField(max_length=10, choices=ACTIVITYTYPE, default='AC')
    Event_Name = models.CharField(max_length=100, blank=True, help_text="Second Term Ball Games or National Choir")
    venue = models.CharField(max_length=100)
    budget = models.IntegerField()
    TripDate = models.DateField()
    TripReturnDate = models.DateField()
    classgoing = models.ForeignKey(Class_Room, on_delete=models.CASCADE)
    Stundent = models.ManyToManyField(Student_Admission,blank=True)
    teacher = models.ManyToManyField(Teacher)
    bus = models.ManyToManyField(Bus)
    busasigned = models.BooleanField()

    class Meta:
        verbose_name_plural = "School Activities"

    def __str__(self):
        return f'{self.type},{self.venue}'
class School_term(models.Model):
    Term_Name =models.CharField(max_length=100)
    Start_Date = models.DateField()
    End_Date = models.DateField()

    def __str__(self):
        return f'{self.Term_Name},{self.Start_Date}'

class Holidays(models.Model):
    Name = models.CharField(max_length=100)
    Holiday_Date = models.DateField()


    def __str__(self):
        return f'{self.Name},{self.Holiday_Date}'
class Half_term(models.Model):
    Name = models.CharField(max_length=100)
    Term = models.ForeignKey(School_term,on_delete=models.CASCADE)
    Start_Date = models.DateField()
    End_Date = models.DateField()

    def __str__(self):
        return f'{self.Name},{self.Term},{self.Start_Date},{self.End_Date}'




