from django.shortcuts import render

# Create your views here.

def mocha(request):
    return render(request, 'pyzza/mocha.html', {})