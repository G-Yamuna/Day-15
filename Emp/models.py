from django.db import models

# Create your models here.
class UsrRg(models.Model):
	username = models.CharField(max_length=120)
	password = models.CharField(max_length=120)
	email = models.CharField(max_length=120)
	age = models.IntegerField(default=10)

	def __str__(self):
		return self.username+" "+self.email

class NewData(models.Model):
	ch=[('M','Male'),('F','Female')]
	mobile = models.IntegerField(default=999999999)
	gender = models.CharField(max_length=10,choices=ch)
	pid = models.OneToOneField(UsrRg,on_delete=models.CASCADE)
# 	username = models.CharField(max_length=120)
# 	# password = models.CharField(max_length=120)
# 	email = models.CharField(max_length=120)
# 	age = models.IntegerField(default=10)
# 	DOB = models.IntegerField()
# 	FatherName = models.CharField(max_length=120)
# 	MotherName = models.CharField(max_length=120)
# 	Qualification = models.CharField(max_length=120)
# 	Occupation = models.CharField(max_length=100)
# 	Address = models.CharField(max_length=200)