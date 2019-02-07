from django.http import HttpResponse
from django.shortcuts import render
import operator

def homePage(request):
    return render(request, 'homePage.html')


def eggs(request):
    return HttpResponse("<h1>here is your egg!</h1>")


def count(request):
    fullText = request.GET['fullText']
    wordList = fullText.split()

    wordDict = {}

    for word in wordList:
        if word in wordDict:
            # increase the number of word
            wordDict[word] += 1
        else:
            # add new word to the dict
            wordDict[word] = 1
    sortedDict = sorted(wordDict.items(), key = operator.itemgetter(1), reverse = True )
    return render(request, 'count.html', {'fullText': fullText, 'count': len(wordList), 'sortedDict': sortedDict })


def about(request):
	return render(request, 'about.html')
