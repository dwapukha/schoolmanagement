# Generated by Django 3.2.6 on 2021-08-16 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_attendance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class_room',
            name='stream',
        ),
        migrations.AlterField(
            model_name='class_room',
            name='class_level',
            field=models.CharField(choices=[('1', 'Year 1'), ('2', 'Year 2'), ('3', 'Year 3'), ('4', 'Year 4')], default='F1', max_length=2),
        ),
        migrations.AlterField(
            model_name='class_room',
            name='name',
            field=models.CharField(choices=[('F1', 'Form One'), ('F2', 'Form Two'), ('F3', 'Form Three'), ('F4', 'Form Four')], default='F1', max_length=4),
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stream', models.CharField(max_length=100)),
                ('classname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.class_room')),
            ],
        ),
        migrations.CreateModel(
            name='ID_Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Admin_No', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student_registration')),
            ],
        ),
    ]
