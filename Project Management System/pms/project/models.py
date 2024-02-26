from django.db import models
from user.models import User

Languages=(
    ('python','python'),
    ('java','java'),
    ('javascript','javascript'),
    ('rust','rust'),
    ('php','php'),
)

class Project(models.Model):
    name=models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100,choices=Languages)
    estimated_hours = models.PositiveIntegerField()
    startDate = models.DateField()
    endDate = models.DateField()
    
    class Meta:
        db_table = "project"
class ProjectTeam(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)        
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
        db_table = "projectteam"
        
class Status(models.Model):
    StatusName=models.CharField(max_length=100)
    
    class Meta:
        db_table="status"
        
class ProjectModule(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE) 
    ModuleName=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    estimeted_time=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    startDate=models.DateField()
    
    
    class Meta:
        db_table="projectModule"
        
priorityChoice=(
    ('High','High'),
    ('Medium','Medium'),
    ('Low','Low'),
)
class Task(models.Model):
    module = models.ForeignKey(ProjectModule,on_delete=models.CASCADE)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.TextField()
    status = models.ForeignKey(Status,on_delete=models.CASCADE)
    totalMinutes=models.IntegerField()
    priority=models.CharField(max_length=50,choices=priorityChoice)
    
    class Meta:
        db_table="task"
class UserTask(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    class Meta:
        db_table="userTask" 
    
