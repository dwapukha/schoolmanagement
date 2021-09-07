from django.db import models
from teachers.models import Teacher
from student.models import Student_Admission

# Create your models here.

class Driver(models.Model):
    name = models.CharField(max_length=200)
    Genderchoice = (
        ('M', 'Male'),
        ('F','Female'),
    )
    age = models.IntegerField()
    Gender = models.CharField(max_length=4, choices=Genderchoice, default='M')
    LicenceNo =models.CharField(max_length=100)
    Contact = models.PositiveIntegerField()
    dateempl =models.DateField()

    def __str__(self):
        return f'{self.name, self.Contact}'

class Conductor(models.Model):
    name = models.CharField(max_length=200)
    Genderchoice = (
        ('M', 'Male'),
        ('F','Female'),
    )
    age = models.IntegerField()
    Gender = models.CharField(max_length=4,choices=Genderchoice, default='M')
    LicenceNo =models.CharField(max_length=100)
    Contact = models.PositiveIntegerField()
    dateempl =models.DateField()
    #BusNo= models.ForeignKey(Bus, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name},{self.Gender}, {self.Contact}'

class Bus(models.Model):
    Bus_Plate_Number = models.CharField(max_length=100)
    Bus_name = models.CharField(max_length=100, blank=True, help_text="Nick Name")
    capacity = models.IntegerField()
    #route = models.ForeignKey(Route, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student_Admission, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Bus_Plate_Number},{self.Bus_name}, {self.capacity}'

class Route(models.Model):
    Route_Name = models.CharField(max_length=100, help_text="Route for the bus should be descriptive")
    pick_point = models.CharField(max_length=100)
    dropoff = models.CharField(max_length=100)
    time = models.TimeField()
    Bus_Number = models.ForeignKey(Bus, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Route_Name},{self.pick_point}, {self.dropoff}, {self.time}'








