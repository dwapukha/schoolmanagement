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
    Cat_One = models.IntegerField(null=True, default=0)
    Cat_Two = models.IntegerField(null=True, default=0)
    Main_Marks = models.IntegerField(null=True, default=0)
    #Grade = models.CharField(max_length=100, editable=False, blank=True)

    def _get_total(self):
        return self.Cat_One + self.Cat_Two + self.Main_Marks
    total = property(_get_total)


    def _get_grade(obj):
        if obj.total >= 80:
            return  "A"
        elif obj.total >= 70:
                return  "A-"
        elif obj.total >= 65:
                return  "B+"
        elif obj.total >= 60:
                return  "B"
        elif obj.total >= 55:
                return  "C+"
        elif obj.total >= 50:
                return  "C"
        elif obj.total >= 45:
                return  "C-"
        elif obj.total >= 40:
                return  "D"
        elif obj.total >= 35:
                return  "E"
        else:
                return "Fail"

    Grade = property(_get_grade)





    def __str__(self):
        return f'{self.studentID}, {self.Cat_One}, {self.Cat_Two},{self.Main_Marks}'

Exam_Result.objects.all()
