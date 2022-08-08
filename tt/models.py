from django.db import models

# Create your models here.
class professor_subject(models.Model):
    prof_subj_id=models.CharField(max_length=400,primary_key=True)
    prof_name=models.CharField(max_length=400)
    subj_name=models.CharField(max_length=400)
    credits=models.IntegerField(default=0)
    class Meta:
        db_table='professor_subject'