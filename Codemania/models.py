from django.db import models

class Problem(models.Model):
	problem = models.CharField(max_length = 5000)
	title = models.CharField(max_length = 10)
	problem_name = models.CharField(max_length = 200)
	test_cases = models.CharField(max_length = 10000)
	correct_answer = models.CharField(max_length = 10000, default = '')
	added_at = models.DateTimeField('Addition Time')
	def __str__(self):
		return self.title
class Problem_submission(models.Model):
	submission = models.CharField(max_length = 4000000)
	problem_title = models.ForeignKey(Problem)
	status = models.CharField(max_length = 20)
	running_time = models.IntegerField()
	submitted_by = models.CharField(max_length = 100)
	submitted_at = models.DateTimeField('Submission Time')
	def __str__(self):
		return self.submitted_by





