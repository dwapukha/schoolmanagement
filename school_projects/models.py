from django.db import models

# Create your models here.
class Upcoming(models.Model):
    name = models.CharField(max_length=200)
    type_of_project = models.CharField(max_length=200)
    start_Date =models.DateField()
    duration = models.IntegerField()
    description = models.TextField(max_length=700)
    budget = models.CharField(max_length=200)
    source_of_funds = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Upcoming Projects"

    def __str__(self):
        return f'{self.name},{self.start_Date}, {self.budget}'

class Projects(models.Model):

    STATUSCHOICES = (
        ('IP', 'in Progress'),
        ('CP', 'Project Completed'),
        ('SP', 'Incomplete Stopped'),
        ('Ab', 'Abandoned'),
        ('Td', 'Tendering Process'),
    )
    name = models.CharField(max_length=200)
    type_of_project = models.CharField(max_length=200)
    start_Date = models.DateField()
    duration = models.IntegerField()
    description = models.TextField(max_length=700)
    budget = models.CharField(max_length=200)
    source_of_funds = models.CharField(max_length=200)
    Project_Status = models.CharField(max_length=10, choices=STATUSCHOICES, default='IP')

    def __str__(self):
        return f'{self.name},{self.start_Date}, {self.budget}'

class Partners(models.Model):
    PARTNER_TYPE = (
        ('AC', 'academic'),
        ('FA', 'Financial'),
        ('SG', 'Social Groups'),
    )
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    partner_type = models.CharField(max_length=20, choices=PARTNER_TYPE, default='AC')

    def __str__(self):
        return f'{self.name},{self.partner_type}'