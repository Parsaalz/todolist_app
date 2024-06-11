from django.urls import path
from . import views
urlpatterns=[
    path('',views.dashboard_page,name="dashboard"),
    path('addtask/',views.addtask_page,name="add_task"),
    path('task/detail/<int:task_id>/',views.detail_task,name="detail_task"),
    path('task/edit/<int:task_id>/',views.edit_task,name="edit_task"),
    path('task/delete/<int:task_id>/',views.delete_task,name="delete_task"),
    path('task/do/<int:task_id>/',views.do_task,name="do"),
    path('task/setalarm/<int:task_id>/',views.setalarmtask,name="setalarmt"),
    path('task/disablealarm/<int:task_id>/',views.disable_alarm,name="disablealarm"),
    path('projects/',views.projects,name="projects"),
    path('projects/<int:project_id>/',views.projects_detail,name="project_detail"),
    path('projects/addproject/',views.add_Project,name="addproject"),
    path('projects/delete/<int:project_id>/',views.delete_project,name="deleteproject"),
    path('projects/Edit/<int:project_id>/',views.Edit_project,name="editproject"),
    path('tasks/today/',views.today_page,name="today_page"),
]