from django.db import models

# Create your models here.
class professor_subject(models.Model):
    prof_subj_id=models.CharField(max_length=400,primary_key=True)
    prof_name=models.CharField(max_length=400)
    subj_name=models.CharField(max_length=400)
    credits=models.IntegerField(default=0)
    class Meta:
        db_table='professor_subject'

class student(models.Model):
    std_id=models.IntegerField(primary_key=True)
    std_name=models.CharField(max_length=500)
    course1=models.CharField(max_length=500)
    course2=models.CharField(max_length=500)
    course3=models.CharField(max_length=500)
    course4=models.CharField(max_length=500)
    course5=models.CharField(max_length=500)
    course6=models.CharField(max_length=500)
    course7=models.CharField(max_length=500)
    course8=models.CharField(max_length=500)
    class Meta:
        db_table='student'
    
class timetable(models.Model):
    Day=models.CharField(max_length=500)
    course1=models.CharField(max_length=500)
    course2=models.CharField(max_length=500)
    course3=models.CharField(max_length=500)
    course4=models.CharField(max_length=500)
    course5=models.CharField(max_length=500)
    course6=models.CharField(max_length=500)
    course7=models.CharField(max_length=500)
    course8=models.CharField(max_length=500)
    course9=models.CharField(max_length=500)
    class Meta:
        db_table='timetable'