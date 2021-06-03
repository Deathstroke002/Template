from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	return render(request, "home.html", {}) #string of HTML code

def contact_view(request, *args, **kwargs):
	my_context = {
	  "my_text": "This is about maintaining a healthy relationship with your colleagues",
	  "my_number": 2,
	  "my_list" : ["Instagram", "Facebook", "Twitter", "WhatsApp", "LinkedIn", "Email"]
	}
	return render(request, "contact.html", my_context) #HTML code