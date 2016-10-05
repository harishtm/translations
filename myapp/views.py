# Create your views here.
from django.shortcuts import render
from forms import Register_Form
from models import Register
from django.utils.translation import ugettext

def home(request):

    form2 = Register_Form()
    reg_list = Register.objects.all()
    msg = ugettext('message from views to be translated')
    return render(request,"home.html",locals())

def contact(request):
    return render(request,"contact.html")

def about_us(request):
    return render(request,"about.html")

def support(request):
    return render(request,"support.html")
