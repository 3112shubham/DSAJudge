from django import forms
from .models import Question, TestCase

class DSAQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'description', 'constraints']

class TestCaseForm(forms.ModelForm):
    class Meta:
        model = TestCase
        fields = ['input_data', 'expected_output', 'question']
