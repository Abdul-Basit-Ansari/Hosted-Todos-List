# from django.db import models
# from django.contrib.auth.models import User

# # Create your models here.


# # Create your models here.

# class todo(models.Model):
# 	"""Model definition for todo."""
# 	sno = models.AutoField(primary_key=True)
# 	title = models.CharField(max_length=100)
# 	user = models.ForeignKey(User,on_delete=models.CASCADE)
# 	desc = models.TextField()
# 	time = models.DateTimeField(auto_now_add=True)
	

# 	class Meta:
# 		"""Meta definition for todo."""

# 		verbose_name = 'todo'
# 		verbose_name_plural = 'todos'

# 	def __str__(self):
# 		return self.title
		
