from django.db import models

class Story11(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	uptated_at = models.DateTimeField(auto_now=True)
	# text.allow_tags = True

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name_plural = "Stories11"
