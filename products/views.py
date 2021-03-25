from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request, *args, **kwargs):
 #return HttpResponse("<h1>Hello World</h1>") #string of HTML code, not actually HTML
    return render(request, "home.html", {})
def contact_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Contact Page</h1>")
    return render(request, "contact.html", {})
def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "this_is_true": True,
        "my_number": 123,
        "my_list": [122,23,45,99, "Abc"],
    }
    return render(request, "about.html", my_context)