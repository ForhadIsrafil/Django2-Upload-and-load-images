from django.db import models

class Pic(models.Model):
	i = models.ImageField(upload_to='media')

	# def __str__(self):
	# 	return self.i
