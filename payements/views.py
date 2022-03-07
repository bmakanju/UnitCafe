from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def UnitCafe(request):
    return HttpResponse(
        "<h1 style='text-align:center;'>Welcome to Unit Cafe</h1><br><div >E-Pin</div><div>Nepa Bill</div>"
    )