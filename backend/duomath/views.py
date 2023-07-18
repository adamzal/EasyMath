from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request, 'duomath/index.html')

def about_us(request):
    return render(request, 'duomath/about_us.html')