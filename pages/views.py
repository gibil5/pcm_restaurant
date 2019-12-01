from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


# ------------------------------------------------ Home ---------------------
def home(request):
	ctx = {}
	output = render(request, 'pages/home.html', ctx)
	return HttpResponse(output)


