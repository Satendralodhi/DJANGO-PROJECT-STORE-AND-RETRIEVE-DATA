from django.http import HttpResponse
from django.shortcuts import render,HttpResponse,redirect
from service.models  import services
# from service.models  import serviceaAdmin

def index(request):
     if request.method=='POST':
        name1=request.POST.get('name')
        m_number1=request.POST.get('m_number')
        email1=request.POST.get('email')
        address1=request.POST.get('address')
        IMG=request.FILES['profile_picture']
      
        savesata=services(name=name1,contactnumber=m_number1,email=email1,address=address1,image=IMG)
        savesata.save()
     return render(request,'index.html')
def dashbord(request):
    ddata=services.objects.all()
    for i in ddata:
        print(i)
    data={
        'ddata':ddata,
    }
    return render(request,'dashbord.html',data)