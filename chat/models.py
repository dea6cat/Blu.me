from django.db import models
from django.conf import settings
from django.utils import timezone

now = timezone.now()

# Create your models here.
class Message(models.Model):
	author 					= models.ForeignKey(settings.AUTH_USER_MODEL, related_name='author_messages', on_delete=models.CASCADE)
	content					= models.TextField(max_length=500, null=False, blank=True)
	timestamp				= models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.author.username

	def last_10_messages(self):
		return Message.objects.order_by('-timestamp'),all()[:10]
