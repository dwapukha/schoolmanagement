import uuid

from django.db import models
import uuid
# Create your models here.
class Student_Registration(models.Model):
    """Model representing an new student"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, help_text='Unique ID for this particular student')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female')

    )
    gender = models.CharField(max_length=1, choices=GENDER, default= 'M')
    #date_of_Admin = models.DateField(auto_now_add=True, editable=False)
    county = models.CharField(max_length=100)
    kcpe_marks = models.IntegerField
    passport = models.ImageField(upload_to='passports/', height_field=None, width_field=None, max_length=100)


    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reversed('Student_Registration-detail', args = [str(self.id)])
    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

class Class_Room(models.Model):
    Class_Names = (
        ('F1', 'Form One'),
        ('F2', 'Form Two'),
        ('F3', 'Form Three'),
        ('F4', 'Form Four'),
    )
    name =models.CharField(max_length=4, choices=Class_Names, default='F1')


    CLASS_LEVEL = (
        ('1', 'Year 1'),
        ('2', 'Year 2'),
        ('3', 'Year 3'),
        ('4', 'Year 4')

    )
    class_level = models.CharField(max_length=2,choices=CLASS_LEVEL, default='F1')

    def __str__(self):
        return f'{self.name}, {self.class_level}'
class Stream(models.Model):
    stream = models.CharField(max_length=100)
    classname  = models.ForeignKey(Class_Room, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.stream}'

class Dormetry(models.Model):
    name = models.CharField(max_length=50)
    cube = models.IntegerField()
    bed_number = models.IntegerField()

    def __str__(self):
        return f'{self.name}, {self.cube}, {self.bed_number}'

class Student_Admission(models.Model):
    Admin_No = models.CharField(max_length=40)
    studenid = models.ForeignKey(Student_Registration, on_delete=models.RESTRICT)
    Class_room = models.ForeignKey(Class_Room, on_delete=models.CASCADE)

    #Student_Name= property(_get_FullName)
    Student_Dorm = models.ForeignKey(Dormetry, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Admin_No}'


class Attendance(models.Model):
    Att_Date = models.DateField()
    Admin_No = models.ForeignKey(Student_Registration, on_delete=models.CASCADE)
    Status = models.BooleanField()
    remark = models.TextField()

    def __str__(self):
        return f'{self.Att_Date},{self.Status}'

class ID_Card(models.Model):
   Student_Name = models.ForeignKey(Student_Registration, on_delete=models.ForeignKey)
   Admin_Number = models.ForeignKey(Student_Admission, on_delete=models.CASCADE)

   def __str__(self):
       return f'{self.Student_Name},{self.Admin_Number}'