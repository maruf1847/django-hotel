from django.db import models

class About(models.Model):
	vission = models.TextField()
	mission = models.TextField()
	image = models.ImageField(upload_to='about/')

	def __str__(self):
		return str(self.id)
