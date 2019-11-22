from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='/admin/login')
def index(request):
    return render(request, 'index.html',{})

# # versao jefferson2
# from django.shortcuts import render
# 
# # Create your views here.
# def index(request):
#     return render(request, 'site_interno/index.html')
