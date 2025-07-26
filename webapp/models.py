from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

class Question(models.Model):
    name = models.CharField(max_length=255, unique=True,null=True)
    link = models.URLField(blank=True, null=True)

    LEVEL_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES, default='Easy')

    def __str__(self):
        return self.name


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20, default='0000')
    branch = models.CharField(max_length=50, default='CSE')
    year = models.IntegerField(default=1)
    college_name = models.CharField(max_length=255, default='')
    project_code = models.CharField(max_length=50, default='')
    leetcode_profile_url = models.URLField(blank=True, null=True)
    leetcode_score = models.IntegerField(default=0)
    leetcode_easy = models.IntegerField(default=0)
    leetcode_medium = models.IntegerField(default=0)
    leetcode_hard = models.IntegerField(default=0)
    github_url = models.URLField(blank=True, null=True)
    codechef_url = models.URLField(blank=True, null=True)
    codeforces_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    codechef_url = models.URLField(blank=True, null=True)
    codeforces_url = models.URLField(blank=True, null=True)
    gfg_url = models.URLField(blank=True, null=True)
    cv_file = models.FileField(
        upload_to='cv_uploads/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.username

# New Contest models
class Contest(models.Model):
    title = models.CharField(max_length=200)
    LEVEL_CHOICES = [
        ('Basic', 'Basic'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]
    category = models.CharField(max_length=100, choices=LEVEL_CHOICES, default='Basic')
    def __str__(self):
        return self.title

class ContestQuestion(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

class ContestParticipation(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    total_score = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.student.user.username} - {self.contest.title}"

class ParticipationQuestion(models.Model):
    participation = models.ForeignKey(ContestParticipation, on_delete=models.CASCADE, related_name="questions")
    contest_question = models.ForeignKey(ContestQuestion, on_delete=models.CASCADE)
    passed_testcases = models.IntegerField(default=0)
    total_testcases = models.IntegerField(default=0)
    is_selected = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.participation.student.user.username} - {self.contest_question.question.name}"
