from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    views = {}
    views['feedbacks'] = Review.objects.all()   #
    return render(request, 'index.html',views)
    views['project'] = Project.objects.all()

def about(request):
    views = {}
    views['feedbacks'] = Review.objects.all()
    return render(request, 'about.html',views)

def services(request):
    return render(request,'services.html')

def protfolio(request):
    return render(request,'protfolio.html')

def price(request):
    return render(request,'price.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        data = Contact.objects.create(
            # field of database in red P
            name = name,
            email = email,
            subject = subject,
            message = message

        )
        data.save()
    return render(request,'contact.html')



