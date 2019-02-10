from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request,'home.html')

def count(request):
    fulltext= request.GET["fulltext"]
    wordslist= fulltext.split()
    no_words= len(wordslist)
    charcount = 0
    for word in wordslist:
        for char in word:
            charcount +=1
    avg_wordlenghth= charcount/no_words

    return render(request,"count.html",{"fulltext":fulltext,"count":len(wordslist),"avg_word":avg_wordlenghth })

def about(request):
    return render(request,"about.html")
