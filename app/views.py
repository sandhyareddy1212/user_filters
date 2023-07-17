from django.shortcuts import render

# Create your views here.
def usdf(request):
    d={'data':'Python proGramming Language is a Very Good Coding Language'}

    return render(request,'usdf.html',d)