from django.db import models
from teachers.models import Subject, Teacher
# Create your models here.
class Ref_Calender(models.Model):
    Day = models.CharField(max_length=100)
    Date_and_Time = models.DateTimeField()

    def __str__(self):
        return 'f{self.Day}, {self.Date_and_Time}'
class Ref_Day(models.Model):
    Day_Name = models.CharField(max_length=100)
    Day_Number = models.IntegerField()

    def __str__(self):
        return 'f{self.Day_Name}, {self.Day_Number}'
class Ref_Subject(models.Model):
    Subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    Subject_Decription = models.CharField(max_length=200)

    def __str__(self):
        return 'f{self.Subject_Decription}'
class Ref_Period(models.Model):
    Period_Start_Time = models.TimeField()
    Period_Start_End = models.TimeField()

    def __str__(self):
        return f'{self.Period_Start_Time}, {self.Period_Start_End}'

class Planned_Timetable(models.Model):
    Schedule_Id = models.AutoField(primary_key=True)
    Day_Name = models.ForeignKey(Ref_Day, null=True, on_delete=models.SET_NULL)
    Period_Number = models.ForeignKey(Ref_Period, null=True, on_delete=models.SET_NULL)
    Subject = models.ForeignKey(Subject, null=True, on_delete=models.SET_NULL)

class Generated_Timetable(models.Model):
    Schedule_Id = models.ForeignKey(Planned_Timetable, on_delete=models.CASCADE)
    Day_Name = models.ForeignKey(Ref_Day, null=True, on_delete=models.SET_NULL)
    Period_Number = models.ForeignKey(Ref_Period, null=True, on_delete=models.SET_NULL)
    Subject = models.ForeignKey(Subject, null=True, on_delete=models.SET_NULL)
    Teacher = models.ForeignKey(Teacher, null=True, on_delete=models.SET_NULL)

class Master_Timetable(models.Model):
    Schedule_Id = models.ForeignKey(Planned_Timetable, on_delete=models.CASCADE)
    Day_Name = models.ForeignKey(Ref_Day, null=True, on_delete=models.SET_NULL)
    Date_Time = models.ForeignKey(Ref_Period, null=True, on_delete=models.SET_NULL)
    #Period_Number = models.ForeignKey(Ref_Period, null=True, on_delete=models.SET_NULL)
    Subject = models.ForeignKey(Subject, null=True, on_delete=models.SET_NULL)
    Teacher = models.ForeignKey(Teacher, null=True, on_delete=models.SET_NULL)


