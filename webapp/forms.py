from django import forms
from .models import Question, Contest , StudentProfile

class DSAQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['name', 'link', 'level']

class ContestForm(forms.ModelForm):
    class Meta:
        model = Contest
        fields = ['title', 'category' ]

class LeetCodeProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['leetcode_profile_url']
        widgets = {
            'leetcode_profile_url': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your LeetCode username'
            })
        }
        labels = {
            'leetcode_profile_url': 'LeetCode Username'
        }

class SocialLinksForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = [
            'leetcode_profile_url',
            'github_url',
            'codechef_url',
            'codeforces_url',
            'linkedin_url',
            'gfg_url',
            'cv_file',  # 🆕 Added CV file upload here
        ]
        widgets = {
            field: forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': f'Enter {field.replace("_url", "").capitalize()} URL'
            }) for field in fields if field != 'cv_file'
        }
        widgets['cv_file'] = forms.FileInput(attrs={
            'class': 'form-control',
            'accept': '.pdf'
        })
        labels = {
            'leetcode_profile_url': 'LeetCode',
            'github_url': 'GitHub',
            'codechef_url': 'CodeChef',
            'codeforces_url': 'Codeforces',
            'linkedin_url': 'LinkedIn',
            'gfg_url': 'GeeksforGeeks',
            'cv_file': 'Upload Your CV (PDF)',
        }

        