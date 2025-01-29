from django.shortcuts import render

from django.http import HttpResponse
def index(request):
    return HttpResponse('Rango says hello partner! <a href="/rango/about/. ">To About Page</a> ')

def about(request):
    return HttpResponse('Rango says here is the about page!. <a href="/rango/. ">To Index Page</a> ')