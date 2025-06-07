from django import forms
from .models import Learner,Grades

class LearnerForm(forms.ModelForm):
    class Meta:
        model = Learner
        fields = ['full_name', 'age', 'email']

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grades
        fields = ['activity_score', 'quiz_score', 'exam_score']
