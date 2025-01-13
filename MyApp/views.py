from django.contrib import messages
from django.shortcuts import render, redirect
from django.conf import settings
from django.shortcuts import reverse
from .forms import ContactForm

# Create your views here.
def new_url(request):
    return redirect(reverse('Home'))

def home(request):
    d = {
        'name' : settings.SITE_OWNER ,
        'title': 'Home'
    }
    return render(request,'index.html',{'context':d})

def header(request):
    d = {
        'name':settings.SITE_OWNER ,
        'title': "Projects"
    }
    return render(request,'projectory.html',{'context':d})

def about(request):
    d = {
        'name':settings.SITE_OWNER,
        'title': "About Me"
    }
    return render(request,'about.html',{'context':d})

def contact(request):
    if request.method == 'POST':
        print("Post message received")
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            print(f"New message from {name},{email}:{message}")
            messages.success(request,"message has been sent successfully")
            return redirect('contact')
        else:
            messages.error(request,"Error in the submission!!!")
    else:
        form = ContactForm()

    d = {
        'name':settings.SITE_OWNER,
        'title': "Contact"
    }    
    return render(request,'contact.html',{'context':d,'form':form})