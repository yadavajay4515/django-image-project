from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib.messages import constants as messages
# Create your views here.
def index(request):
    context={
        "variable":"ajay yadav os",
        "variable1":"Ajay is grate"
    }
    # messages.SUCCESS(request,"this  Ajay yadav bhai")
    # messages.success(request, 'Your massage ajay yadav') 
    # messages.SUCCESS(request,"this success massage")
#   massages.success(request,"this is success massage")
    return render(request,'index.html',context)
    # return HttpResponse("this is Ajay yadav home page") 
 

def aboute(request):
    return render(request,'aboute.html')
    # return HttpResponse("this is about page")


def contact(request):
      if request.method == "POST":
           name = request.POST.get('name')
           email = request.POST.get('email')
           phone = request.POST.get('phone')
           desc = request.POST.get('desc')  
           con = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
           con.save()   
        #    messages.success(request, 'Your massage have be sent')      
      return render(request,'contact.html') 
    # return HttpResponse("this is contect page")

def services(request):
      return render(request,'services.html')
    # return HttpResponse("this is services page")



