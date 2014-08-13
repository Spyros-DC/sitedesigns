from django.shortcuts import render
from django.template import Context
from models import Story11
from sitedesigns.forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

def index(request, template_name):
    s = Story11.objects.all()
    context = Context({'s':s, 'class':'' })
    return render(request, template_name, context)

def contact(request, template_name):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['sitedesigns17@gmail.com'],
            )
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()
    s = Story11.objects.all()    
    context = Context({'s':s, 'form':form, 'class':'class="contact_emphasis"'})
    return render(request, template_name, context)

def systaseis(request, template_name):
    s = Story11.objects.all()
    context = Context({'s':s, 'class':'class="systaseis_emphasis"' })
    return render(request, template_name, context)


def works(request, template_name):
    s = Story11.objects.all()
    context = Context({'s':s, 'class':'class="works_emphasis"' })
    return render(request, template_name, context)
