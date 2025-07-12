from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    constraints = models.TextField()

class TestCase(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='testcases')
    input_data = models.TextField()
    expected_output = models.TextField()

    def __str__(self):
        return f"Testcase for {self.question.title}"

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20, default='0000')
    branch = models.CharField(max_length=50, default='CSE')
    year = models.IntegerField(default=1)  # <-- added default here

    def __str__(self):
        return self.user.username

