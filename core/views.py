from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets

from .models import Learner, Subjects, Grades
from .serializers import LearnerSerializer, SubjectsSerializer, GradesSerializer
from .forms import LearnerForm, GradeForm

# ==========================
# API ViewSets (DRF)
# ==========================

class LearnerViewSet(viewsets.ModelViewSet):
    queryset = Learner.objects.all()
    serializer_class = LearnerSerializer

class SubjectsViewSet(viewsets.ModelViewSet):
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer

class GradesViewSet(viewsets.ModelViewSet):
    queryset = Grades.objects.all()
    serializer_class = GradesSerializer

# ==========================
# Core Views
# ==========================

def index(request):
    learners = Learner.objects.all()
    return render(request, 'index.html', {'learners': learners})

def contact_view(request):
    return render(request, 'contact.html')

def student_info(request, pk):
    learner = get_object_or_404(Learner, pk=pk)
    return render(request, 'student_info.html', {'learner': learner})

# ==========================
# Learner Views
# ==========================

def add_learner(request):
    if request.method == 'POST':
        form = LearnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = LearnerForm()
    return render(request, 'add_learner.html', {'form': form})

def update_learner(request, pk):
    learner = get_object_or_404(Learner, pk=pk)
    if request.method == 'POST':
        learner.full_name = request.POST.get('full_name')
        learner.age = request.POST.get('age')
        learner.email = request.POST.get('email')
        learner.save()
        return redirect('student_info', pk=learner.id)
    return render(request, 'update_student.html', {'learner': learner})

def delete_learner(request, pk):
    learner = get_object_or_404(Learner, pk=pk)
    if request.method == 'POST':
        learner.delete()
        return redirect('index')
    return render(request, 'delete_student.html', {'learner': learner})

# ==========================
# Subject Views
# ==========================

def update_subject(request, pk):
    subject = get_object_or_404(Subjects, pk=pk)
    if request.method == 'POST':
        subject.title = request.POST.get('title')
        subject.save()
        return redirect('student_info', pk=subject.learner.id)
    return render(request, 'update_subject.html', {'subject': subject})

def delete_subject(request, pk):
    subject = get_object_or_404(Subjects, pk=pk)
    learner_id = subject.learner.id
    if request.method == 'POST':
        subject.delete()
        return redirect('student_info', pk=learner_id)
    return render(request, 'delete_subject.html', {'subject': subject})

# ==========================
# Grade Views
# ==========================

def update_grade(request, pk):
    grade = get_object_or_404(Grades, pk=pk)
    if request.method == 'POST':
        grade.activity_score = request.POST.get('activity_score')
        grade.quiz_score = request.POST.get('quiz_score')
        grade.exam_score = request.POST.get('exam_score')
        grade.save()
        return redirect('student_info', pk=grade.subjects.learner.id)
    return render(request, 'update_grade.html', {'grade': grade})

def add_grade(request, subject_id):
    subject = get_object_or_404(Subjects, id=subject_id)
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            grade = form.save(commit=False)
            grade.subjects = subject
            grade.save()
            return redirect('student_info', pk=subject.learner.id)
    else:
        form = GradeForm()
    return render(request, 'add_grade.html', {'form': form, 'subject': subject})

def delete_grade(request, pk):
    grade = get_object_or_404(Grades, pk=pk)
    learner_id = grade.subjects.learner.id
    if request.method == 'POST':
        grade.delete()
        return redirect('student_info', pk=learner_id)
    return render(request, 'delete_grade.html', {'grade': grade})
