from django.db import models

class Learner(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.full_name

class Subjects(models.Model):  
    title = models.CharField(max_length=100)
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE, related_name='subjects')

    def __str__(self):
        return f"{self.title} - {self.learner.full_name}"

class Grades(models.Model):  
    subjects = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='grades')
    activity_score = models.FloatField()
    quiz_score = models.FloatField()
    exam_score = models.FloatField()

    def __str__(self):
        return f"{self.subjects.title} - Grades"
