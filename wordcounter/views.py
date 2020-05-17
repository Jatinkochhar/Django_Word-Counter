from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render (request, 'home.html')
def count(request):
    fulltext1 = request.GET['fulltext']
    wordlist = fulltext1.split()
    return render(request,'count.html', {'fulltext':fulltext1,'count_of_text':len(wordlist)})
def about(request):
    return render(request, 'About.html')