from django.db import models

class Teacher(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	id_number=models.IntegerField()
	registration_number=models.CharField(max_length=50)
	place_of_residence=models.CharField(max_length=50)
	phone_number=models.CharField(max_length=50)
	email=models.EmailField(max_length=50)
	date_joined=models.DateField()
	profession=models.CharField(max_length=50)
	image=models.ImageField(upload_to="teacher_image",blank=True)	

	def __str__(self):
		return self.first_name