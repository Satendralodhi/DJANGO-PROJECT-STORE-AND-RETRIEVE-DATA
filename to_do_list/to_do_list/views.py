from django.http import HttpResponse
from django.shortcuts import render,HttpResponse,redirect
from service.models  import service
def index(request):
     me=['COMPLETED','UNCOMPLETED']
     taskstatus2=''
     if request.method=='POST':
        name1=request.POST.get('name')
        m_number1=request.POST.get('m_number')
        email1=request.POST.get('email')
        taskname1=request.POST.get('taskname')
        taskstatus1=request.POST.get('taskstatus')
        if  taskstatus1==me[0]:
            taskstatus2=me[0]
        elif taskstatus1==me[1]:
            taskstatus2=me[1]
        savesata=service(name=name1,contactnumber=m_number1,email=email1,taskname=taskname1,mark=taskstatus2)
        savesata.save()
     return render(request,'index.html')
def dashbord(request):
    ddata=service.objects.all()
    for i in ddata:
        print(i)
    data={
        'ddata':ddata,
    }
    return render(request,'dashbord.html',data)
def update(request ,myid):
    ddata=service.objects.get(id=myid)
    data={
        'ddata':ddata
    }
    return render(request,'index.html',data)
def delete(request,myid):
    ndata=service.objects.get(id = myid)
    ndata.delete()
    return redirect(dashbord)
def u(request,myid):
    ndata=service.objects.get(id = myid)
    
    if request.method=='POST':
        ndata.name=request.POST['name']
        ndata.contactnumber=request.POST.get('m_number')
        ndata.email=request.POST.get('email')
        ndata.taskname=request.POST.get('taskname')
        ndata.taskstatus=request.POST.get('taskstatus')
        ndata.save()
    return redirect(dashbord)