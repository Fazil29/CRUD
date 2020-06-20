from django.db import models

# Create your models here.
class Footballers(models.Model):
    F_id = models.IntegerField(primary_key=True)
    F_name = models.CharField(max_length=100)
    F_salary = models.IntegerField()
    F_goals = models.IntegerField()
    objects = models.Manager()
    class Meta:
        db_table = "Footballers"
