from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    numbers = [1,2,3,4]
    name = "Denmark Garcia"
    args = {
       'myname': "Denmark Garcia",
       'course':'Computer Science'

   }
    return render(request,'accounts/home.html',args)
