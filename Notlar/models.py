from django.db import models
from django.conf import settings


class Course(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='courses')
	name = models.CharField(max_length=200)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		unique_together = ('user', 'name')

	def __str__(self):
		return f"{self.name} ({self.user.username})"


class Note(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notes')
	course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, related_name='notes')
	title = models.CharField(max_length=200, blank=True)
	content = models.TextField(blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.title or 'Untitled'} - {self.user.username}"
