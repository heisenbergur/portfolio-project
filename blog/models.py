from django.db import models

class Blog(models.Model):
	image=models.ImageField(upload_to='images/')
	title=models.CharField(max_length=50)
	pub_date=models.DateField(auto_now_add=True)
	body=models.CharField(max_length=500)

