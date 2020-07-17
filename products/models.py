from django.db import models
import time
from datetime import date
from django.contrib.auth.models import User


# Product Class
class Product(models.Model):

	title=models.CharField(max_length=50)
	url=models.TextField()
	pub_date=models.DateTimeField()
	votes_total=models.IntegerField(default=1)
	image=models.ImageField(upload_to='images/')
	icon=models.ImageField(upload_to='images/')
	body=models.TextField()
	pub_date_pretty=models.DateTimeField()
	hunter=models.ForeignKey(User,on_delete=models.CASCADE)
#TODO
#pub_date_pretty
#hunter

	def __str__(self):
			return self.title
		
		def __str__(self):
			return self.url
		
		def __str__(self):
			return self.pub_date
		
		def __str__(self):
			return self.votes_total

		def __str__(self):
			return self.image
			
		def __str__(self):
			return self.icon

		def summary(self):
			return self.body[:200]
			
		def pub_date_pretty
			return self.pub_date.strftime('%b %e %y')