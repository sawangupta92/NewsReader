from django.db import models
class feed(models.Model):
	description=models.CharField(max_length=1000)
	date=models.DateTimeField(auto_now=True, auto_now_add=True, db_index=True)
	# class Meta:
	# 	ordering=['-date']
# Create your models here.
