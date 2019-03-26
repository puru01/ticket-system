from django.db import models
import uuid
# Create your models here.
class Ticket(models.Model):
	#tid = models.IntegerField(primary_key=True)
	t_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	ttype = models.CharField(max_length=50, default='Incident')
	category = models.CharField(max_length=50, default='Other')
	#subcategory = models.CharField(max_length=50)
	title = models.CharField(max_length=50)
	priority = models.CharField(max_length=10, default='Normal')
	status = models.CharField(max_length=20, default='Open')
	requestuser = models.CharField(max_length=50, default="System Admin")
	processmanager  = models.CharField(max_length=50, default="System Admin")

