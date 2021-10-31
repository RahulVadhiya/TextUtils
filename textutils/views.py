# i have created this file - 'rahul'
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
    #return HttpResponse('''<h1>hello rahul bhai /br Home</h1>  ''')

def ContactUs(request):
    return render(request,'ContactUs.html')

def analyze(request):
    #FOR TEXT AREA
    djtext = request.POST.get('text','default')

    #Checking CHECKBOX value
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    lowercase = request.POST.get('lowercase','off')
    charcount = request.POST.get('charcount','off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext = analyzed
        #return render(request,'analyze.html',params)


    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed To Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if (lowercase == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.lower()
        params = {'purpose': 'Changed To lower', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n":
                analyzed = analyzed + char
            params = {'purpose': 'Removed New Line', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)


    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

            params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)


    if (charcount == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " "):
                analyzed = analyzed + char
            params = {'purpose': 'Char Length','analyzed_text': len(analyzed)}


    if(removepunc != "on" and fullcaps!="on" and lowercase != "on" and newlineremover != "on" and extraspaceremover != "on" and charcount != "on"):
        return HttpResponse("PLEASE SELECT THE OPERATION")


    return render(request, 'analyze.html', params)







