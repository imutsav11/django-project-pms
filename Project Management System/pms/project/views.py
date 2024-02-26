from django.shortcuts import render

from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView,DetailView
from .forms import ProjectCreationForm,ProjectTeamCreationForm,ProjectModuleCreationForm,ProjectTaskCreationForm
from .models import Project,ProjectTeam,ProjectModule,Task

# Create your views here.

class ProjectCreationView(CreateView):
    template_name = 'project/project_create.html'
    model = Project
    form_class = ProjectCreationForm
    success_url = '/project/list/'
    
class ProjectListView(ListView):
    template_name = 'project/project_list.html'
    model = Project
    context_object_name = 'projects'
    
class ProjectDetaileView(DetailView):
    model=Project
    context_object_name="project"
    template_name='project/project_detail.html'

class ProjectDeleteView(DeleteView):
    model=Project
    template_name='project/project_delete.html'
    success_url="project/project_list/"
    
class ProjectUpdateView(UpdateView):
    model=Project
    form_class=ProjectCreationForm
    template_name='project/project_update.html'
    success_url="project/project_list"
    
class ProjectTeamCreateView(CreateView):    
    template_name = 'project/team_create.html'
    model = ProjectTeam
    success_url = '/project/list/'
    form_class = ProjectTeamCreationForm
    
class ProjectTeamListVIew(ListView):
    template_name='project/team_list.html'
    context_object_name="teams"
    model=ProjectTeam
    context_object_name='projects'
    
class ProjectTeamDetaileView(DetailView):
    model=ProjectTeam
    context_object_name="project"
    template_name='project/team_detail.html'

class ProjectTeamDeleteView(DeleteView):
    model=ProjectTeam
    template_name='project/team_delete.html'
    success_url="project/team_list/"
    
class ProjectTeamUpdateView(UpdateView):
    model=Project
    form_class=ProjectTeamCreationForm
    template_name='project/team_update.html'
    success_url="project/team_list"
    
class ProjectModuleCreateView(CreateView):
    template_name = 'project/module_create.html'
    model= ProjectModule
    success_url = '/project/ModuleList'
    form_class = ProjectModuleCreationForm

class ProjectModuleListView(ListView):
    template_name = 'project/module_list.html'
    model = ProjectModule
    context_object_name = 'projects'

class ProjectTaskCreateView(CreateView):
    template_name='project/taskcreate.html'
    model=Task
    success_url='/project/TaskList'
    form_class=ProjectTaskCreationForm    
    
class ProjectTaskListView(ListView):
    template_name = 'project/tasklist.html'
    model = Task
    context_object_name = 'Projects'