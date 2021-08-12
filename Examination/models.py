from django.db import models
from student.models import Student_Admission
from teachers.models import Subject
# Create your models here.
class Exam_Type(models.Model):
    Exam_type = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Exam Types"

    def __str__(self):
        return f'{self.name}, {self.Exam_type}'
class Exam(models.Model):
    Exam_type = models.ForeignKey(Exam_Type, on_delete=models.CASCADE)
    start_Date = models.DateField()

    def __str__(self):
        return f'{self.start_Date}, {self.Exam_type}'
class Grade(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}, {self.description}'

class Exam_Result(models.Model):
    examID = models.ForeignKey(Exam, on_delete=models.CASCADE)
    studentID = models.ForeignKey(Student_Admission, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    Catonemarks = models.IntegerField(null=True, default=0)
    Cattwomarks = models.IntegerField(null=True, default=0)
    Mainmarks = models.IntegerField(null=True, default=0)


    def __str__(self):
        return f'{self.studentID}, {self.Catonemarks}, {self.Cattwomarks},{self.Mainmarks}'

Exam_Result.objects.all()
