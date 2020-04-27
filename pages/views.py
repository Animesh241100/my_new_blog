from django.http import HttpResponse #no need if you are making use of 'render' to render .html files.

from django.shortcuts import render


def home_view(request, *args, **kwargs):
    #print(request.user) #uncomment to print which user is logged in
    #print(request) #uncomment to print the request.
    #return HttpResponse("<h1>Welcome to My home page using Python-Django.</h1><body bgcolor = 'red'> </body>")

    #instead of writing one-line string codes of HTML, we are gonna use some of the 
    # Django_shortcuts, look when we created the app itself the Django-admin has already 
    # imported the 'render' from 'django.shortcuts', so we use this in-built render to render a
    #  whole fuckin' .html document itself. Wow, that's what you were waiting for.
    return render(request, "home.html", {})

def present_view(request, *args, **kwargs):
    present_context = {  #this is a context dictionary
        "my_college_id": "ced18i065",  #this values can be accessed at .html file by using
        "Mob"          : 7986554,      #the keys as a context variable in there.
        "Friends_list" : ['Ram', 'Raj', 'Shiv', True, 12, False],
        "is_true"      : True,
        "is_false"     : False
    
    }
    return render(request, "present.html", present_context)

def file1_view(request, *args, **kwargs):
    return render(request, "File1.html", {}) 

# Create your views here.
