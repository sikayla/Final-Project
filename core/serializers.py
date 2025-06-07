from rest_framework import serializers
from .models import Learner, Grades, Subjects

class GradesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grades
        fields = '__all__'

class SubjectsSerializer(serializers.ModelSerializer):
    grades = GradesSerializer(many=True, read_only=True)
    class Meta:
        model = Subjects
        fields = '__all__'

class LearnerSerializer(serializers.ModelSerializer):
    subjects = SubjectsSerializer(many=True, read_only=True)
    class Meta:
        model = Learner
        fields = '__all__'
