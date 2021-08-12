# Generated by Django 3.2.6 on 2021-08-06 19:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class_Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('stream', models.CharField(max_length=100)),
                ('class_level', models.CharField(choices=[('F1', 'Form One'), ('F2', 'Form Two'), ('F3', 'Form Three'), ('F4', 'Form Four')], default='F1', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Dormetry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student_Registration',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, help_text='Unique ID for this particular student', primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('date_of_Admin', models.DateField(blank=True, null=True)),
                ('county', models.CharField(max_length=100)),
                ('passport', models.ImageField(upload_to='passports/')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Student_Admission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Admin_No', models.CharField(max_length=40)),
                ('Class_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.class_room')),
                ('Student_Dorm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.dormetry')),
                ('studenid', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='student.student_registration')),
            ],
        ),
    ]
