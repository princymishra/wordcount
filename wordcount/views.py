from django.http import HttpResponse
from django.shortcuts import render

def homepage(request): #request ka arg url se aa rha h
    return render(request,'home.html')

def count(request):
    fulltext = request.GET["fulltext"] #getting the entered value from the url
    wordlist = fulltext.split()
    charNo =0
    for word in wordlist:
        for char in word:
           charNo +=1
    average = charNo/len(wordlist)
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'average':average})


def about(request):
    return render(request,'about.html')