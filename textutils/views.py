from  django.http import HttpResponse
from  django.shortcuts import render

def index(request):
    return render(request, 'index.html',)

def analyze(request):
    djtext = request.POST.get('text')

    # Check Box Values
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcounter = request.POST.get('charcounter','off')

#=================== Punctuations Remover Function =========================================
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose' : 'Remove Punctuations', 'analyzed_text' : analyzed}
        return render(request,'analyze.html', params)

#==================== Uppercase Funtion ====================================================
    elif (fullcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed +char.upper()
        params = {'purpose': 'Change To UPPERCASE', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

#====================== Extra Space Remover =================================================
    elif (extraspaceremover == 'on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == "  "  and  djtext[index+1] =="  "):
                analyzed = analyzed +char
        params = {'purpose': 'Remove Extra Spaces', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

#======================== New Line Remover Funtion===========================================
    elif (newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char != '\n' and char!='\r':
                analyzed = analyzed +char
        params = {'purpose': 'Remove NewLines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

#=========================Character Counter Function ===========================================
    elif (charcounter == 'on'):
        analyzed = ""
        analyzed = len(djtext)
        params = {'purpose': 'Character Counter', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")
