from django.shortcuts import redirect, render

from app.models import Student

# Create your views here.
def index(request):
    data=Student.objects.all()
    return render(request,'app/index.html',{'data':data})
def insertdata(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        query=Student(name=name,email=email,age=age,gender=gender)
        query.save()
        return redirect("/")
    return render(request,'app/index.html')
def updateData(request,id):
    d=Student.objects.get(id=id)
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        x=Student.objects.get(id=id)
        x.name=name
        x.email=email
        x.gender=gender
        x.age=age
        x.save()
        return redirect("/")
    return render(request,'app/edit.html',{'d':d})