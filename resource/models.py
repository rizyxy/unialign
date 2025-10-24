from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    learning_outcome = models.TextField()
    content = models.TextField(null=True)

class SkillFramework(models.Model):
    name = models.CharField(max_length=255)

class Skill(models.Model):
    skill_framework_id = models.ForeignKey(SkillFramework, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()


