from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    worddict = {}

    for word in wordlist:
        worddict[word] = worddict.get(word, 0) + 1

    sortedwords = sorted(worddict.items(), key = lambda x: x[1], reverse = True)

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'worddict':sortedwords})

def about(request):
    return render(request, 'about.html')
