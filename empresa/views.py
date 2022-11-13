from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def nova_empresa(request): #funcoa a ser retornada no urls

    return render(request, 'nova_empresa.html')