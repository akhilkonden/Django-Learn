from django.shortcuts import render
from django.http import HttpResponse
from .models import detail
# Create your views here.
from .models import student

def page1(request):
    return HttpResponse("Hello All")

def page2(request):
    return HttpResponse("welcome")
def  page3(request):
    string = "Hello Wolrd"
    l = ['akhil', 'rogersoft', 'python fullstack','kochi','asus book','software developer']
    return render(request,'html.html',{'k1':string, 'k2':l})
# def page4(request):
#     p1 = detail()
#     p1.name = "akhil"
#     p1.age = 21
#     p1.rollno = 16
#     p2 = detail()
#     p2.name = "amith"
#     p2.age = 20
#     p2.rollno = 15
#     p3 = detail()
#     p3.name = "dop"
#     p3.age = 23
#     p3.rollno = 17
#     l = [p1,p2,p3]
#
#     return render(request,'table.html',{"detail":l})

def page5(request):
    if request.method == "POST":
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        if 'add' in request.POST:
            result = int(num1) + int(num2)
            return render(request, "form.html", {'OUTPUT': result})
    return render(request,'form.html')
def form1(request):
    if request.method =='POST':
        if request.POST.get('name1')and request.POST.get('name2'):
            post = student()
            post.name = request.POST.get('name1')
            post.address = request.POST.get('name2')
            post.save()
            # return render(request,'form1.html')
            objectname = student.objects.all()
            return render(request, 'form1.html', {'KEY': objectname})
    objectname = student.objects.all()
    return render(request,'form1.html',{'KEY':objectname})



