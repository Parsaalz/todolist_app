from django.shortcuts import render,redirect
from .forms import TaskForm,ProjectForm,AlarmTaskForm
from .models import TaskUsers,Projects
from accounts.models import UserPic
from django.contrib.auth.decorators import login_required
from datetime import datetime,timedelta,date
@login_required
def dashboard_page(request):
    ts=TaskUsers.objects.filter(user=request.user,do=False,dead_line__gte=datetime.now()).order_by('dead_line')[:8]
    ts_did=TaskUsers.objects.filter(user=request.user,do=True).order_by('dead_line')[:8]
    ##get date for know finished task time or nor
    date_now=datetime.now()
    date_three_days=timedelta(days=4)
    date_now+=date_three_days
    #get time and date for show alarm
    time_now = datetime.now()
    current_time = datetime.today().strftime('%H:%M')
    current_date=date.today()

    ts_little=TaskUsers.objects.filter(dead_line__gte=datetime.now(),dead_line__lte=date_now,do=False).order_by('dead_line')[:8]
    image_profile=UserPic.objects.get(user=request.user)
    ts_timefinished=TaskUsers.objects.filter(user=request.user,do=False,dead_line__lt=datetime.now()).order_by('dead_line')[:8]
    al=[]
    sr=[]
    search_name = request.GET.get("sr")
    if search_name:
        sr=TaskUsers.objects.filter(user=request.user,title__icontains=search_name)
    for i in ts:
        if i.alarm_d is not None and i.alarm_d == current_date:
            al.append(i)
        elif i.alarm_d is not None and i.alarm_d > current_date:
            al.append(i)
    context={
        "ts":ts,"image_profile":image_profile,
        "ts_did":ts_did,
        "ts_little":ts_little,
        "ts_time":ts_timefinished,
        "al":al,
        "sr":sr,
    }
    return render(request,'dashboard.html',context)
@login_required
def addtask_page(request):
    image_profile=UserPic.objects.get(user=request.user)
    task_form=TaskForm()
    if request.method=='POST':
        task_form=TaskForm(data=request.POST)
        if task_form.is_valid():
            title_t=task_form.cleaned_data.get('title')
            description_t=task_form.cleaned_data.get('description')
            dead_line_t=task_form.cleaned_data.get('dead_line')
            new_task=TaskUsers.objects.create(user=request.user,title=title_t,description=description_t)
            new_task.dead_line=dead_line_t
            new_task.save()
            return redirect('dashboard')
    context={
        "form":task_form,"image_profile":image_profile,
    }
    return render(request,'addtask.html',context)

@login_required
def detail_task(request,task_id):
    image_profile=UserPic.objects.get(user=request.user)
    tsdt=TaskUsers.objects.get(id=task_id)
    context={
        "tsdt":tsdt,"image_profile":image_profile,
    }
    return render(request,'detail_task.html',context)


@login_required
def edit_task(request,task_id):
    image_profile=UserPic.objects.get(user=request.user)
    this=TaskUsers.objects.get(id=task_id)
    ts=TaskForm(initial={"title":this.title,"description":this.description,"dead_line":this.dead_line})
    if request.method=='POST':
        ts=TaskForm(data=request.POST)
        if ts.is_valid():
            title_t=ts.cleaned_data.get('title')
            description_t=ts.cleaned_data.get('description')
            date_t=ts.cleaned_data.get('dead_line')
            new=TaskUsers.objects.get(id=task_id)
            new.title=title_t
            new.description=description_t
            new.dead_line=date_t
            new.save()
            return redirect('dashboard')
    context={
        "ts":ts,"image_profile":image_profile,
    }
    return render(request,'edit_task.html',context)

@login_required
def delete_task(request,task_id):
    this=TaskUsers.objects.get(id=task_id)
    this.delete()
    return redirect('dashboard')
@login_required
def do_task(request,task_id):
    this=TaskUsers.objects.get(id=task_id)
    this.do=True
    this.save()
    return redirect('dashboard')

@login_required
def projects(request):
    image_profile=UserPic.objects.get(user=request.user)
    pr=Projects.objects.filter(user=request.user)[:8]
    pr_f=Projects.objects.filter(user=request.user)[:8]
    flag=1
    for i in pr_f:
        flag=1
        for j in i.tasks.all():
            if j.do==False:
                print("yes")
                flag=0
                break
        if flag==0:
            i.do=False
            i.save()
        else:
            i.do=True
            i.save()
    context={
        "pr":pr,"image_profile":image_profile,
    }
    return render(request,'projects.html',context)

def projects_detail(request,project_id):
    pr=Projects.objects.get(id=project_id)
    image_profile=UserPic.objects.get(user=request.user)
    context={
        "pr":pr,"image_profile":image_profile,
    }
    return render(request,"projects_detail.html",context)



def add_Project(request):
    pf=ProjectForm()
    image_profile=UserPic.objects.get(user=request.user)
    if request.method=="POST":
        pf=ProjectForm(data=request.POST)
        if pf.is_valid():
            title_t=pf.cleaned_data.get('title')
            tasks_t=pf.cleaned_data.get('tasks')
            date_t=pf.cleaned_data.get('dead_line')
            new=Projects.objects.create(user=request.user,title=title_t,dead_line=date_t)
            new.tasks.set(tasks_t)
            new.do=False
            new.save()
            return redirect('projects')
    context={
        "pf":pf,"image_profile":image_profile,
    }
    return render(request,"add_project.html",context)


def delete_project(request,project_id):
    pr=Projects.objects.get(id=project_id)
    pr.delete()
    return redirect('projects')

def Edit_project(request,project_id):
    pr=Projects.objects.get(id=project_id)
    fp=ProjectForm(initial={"title":pr.title,"tasks":pr.tasks.all(),"dead_line":pr.dead_line})
    if request.method=="POST":
        fp=ProjectForm(data=request.POST)
        if fp.is_valid():
            title_t=fp.cleaned_data.get('title')
            tasks_t=fp.cleaned_data.get('tasks')
            date_t=fp.cleaned_data.get('dead_line')
            pr.title=title_t
            pr.tasks.set(tasks_t)
            pr.date_t=date_t
            pr.save()
            return redirect('projects')
    context={
        "pf":fp,
    }
    return render(request,'add_project.html',context)


def setalarmtask(request,task_id):
    ts=TaskUsers.objects.get(id=task_id)
    tf=AlarmTaskForm(initial={"alarm_d":ts.alarm_d,"alarm_t":ts.alarm_t})
    if request.method=="POST":
        tf=AlarmTaskForm(data=request.POST)
        print("yas")
        if tf.is_valid():
            alarm_dd=tf.cleaned_data.get('alarm_d')
            alarm_tt=tf.cleaned_data.get('alarm_t')
            ts.alarm_d=alarm_dd
            ts.alarm_t=alarm_tt
            ts.save()
            return redirect('dashboard')
    context={
        "tf":tf,
    }
    return render(request,'setalarmtask.html',context)



def disable_alarm(request,task_id):
    ts=TaskUsers.objects.get(id=task_id)
    ts.alarm_d=None
    ts.alarm_t=None
    ts.save()
    return redirect('dashboard')


def today_page(request):
    ts_today=TaskUsers.objects.filter(dead_line=datetime.today())
    image_profile=UserPic.objects.get(user=request.user)
    context={
        "ts_today":ts_today,
        "image_profile":image_profile,
    }
    return render(request,'today.html',context)