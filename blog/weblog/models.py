from django.db import models

# Create your models here.

class Topic(models.Model):
	#分类
	topics = models.CharField(max_length=50, default="")
	
	def __str__(self):
		return self.topics
		
class Entry(models.Model):
	#文章
	own_topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	own_title = models.CharField(max_length=60, default="")
	own_text = models.TextField()
	add_date = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.own_text[:30] + "... ..."

class Tag(models.Model):
	#标签
	tags = models.CharField(max_length=50, default="")
	tagstotopics = models.ManyToManyField(Entry)
	
	def __str__(self):
		return self.tags