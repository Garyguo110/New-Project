from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

class Workflow(models.Model):
	name = models.CharField(max_length=200)
	url = models.CharField(max_length=200)
	create_at = models.DateTimeField('date created')
	is_active = models.BooleanField(default=False)

class Step(models.Model):
	workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE)

	class Meta:
		order_with_respect_to = 'workflow'
		abstract = True

class WebClickStep(Step):
	selector = models.CharField(max_length=200)

class WebFillStep(Step):
	selector = models.CharField(max_length=200)
	value = models.TextField()

class WebReadStep(Step):
	selector = models.CharField(max_length=200)
	parser = models.CharField(max_length=200)

class SendSmsStep(Step):
      phone_number = models.CharField(max_length=200)
      value = models.CharField(max_length=200)
