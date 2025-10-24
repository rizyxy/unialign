from django.db import models
from resource.models import Course, Skill

# Create your models here.

class ExtractedCourse(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    extracted_skills = models.TextField(null=True)

class ExtractedSkill(models.Model):
    skill_id = models.ForeignKey(Skill, on_delete=models.CASCADE)
    extracted_skills = models.TextField()