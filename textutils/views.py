# MY creation
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
    #return HttpResponse('<h1>Disco</h1><a href="https://www.facebook.com/saurav.sharma.77770194/"> Facebook </a> <br> <br>'
      #                  ' <a margin="10px" href="https://twitter.com/sauravsharma60"> Twitter </a>')
#def about(request):
#    return HttpResponse('hello')
#def facebook(request):
 #   return HttpResponse()
#def spaceremove(request):
 #    return HttpResponse("space remove")
#def removepunc(request):
 #    djtext=request.GET.get('text','default')
  #   return HttpResponse("removepunc")
#def capfirst(request):
 #    return HttpResponse("capfirst")
#def newlineremove(request):
 #    return HttpResponse("newlineremove <br> <a href='/'> home</a>")
#def charcount(request):
 #    return HttpResponse("charcount")
def analyze(request):
     djtext = request.POST.get('text', 'default')
     removepunc = request.POST.get('removepunc', 'off')
     fullcaps = request.POST.get('fullcaps', 'off')
     newlineremover = request.POST.get('newlineremover', 'off')
     extraspaceremover = request.POST.get('extraspaceremover', 'off')
     charcount = request.POST.get('charcount', 'off')
     #print(removepunc)
     #print(djtext)
     #analyzed=djtext
     fin=djtext
     purpose=""
     if removepunc == 'on':
          punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_+~_'''
          analyzed=''
          for char in djtext:
               if char not in punctuations:
                    analyzed=analyzed+char
          fin=analyzed
          purpose=purpose+"Remove Punctuation"
          param={'purpose': 'Remove Punctuation', 'analyzed_text': analyzed}
         # return render(request,'analyze.html',param)
     if fullcaps == 'on':
          analyzed = ''
          for char in fin:
               analyzed=analyzed+char.upper()
          fin=analyzed
          purpose=purpose+"Capitalize"
          param = {'purpose': 'Capitalise it', 'analyzed_text': analyzed}
          #return render(request, 'analyze.html', param)
     if extraspaceremover == 'on':
          analyzed = ''
          for index,char in enumerate(fin):
               if not (fin[index] == " " and fin[index+1]==" "):
                    analyzed=analyzed + char
          fin=analyzed
          purpose = purpose + "Space Counter"
          param = {'purpose': 'Extra Space Removed', 'analyzed_text': analyzed}
          #return render(request, 'analyze.html', param)
     if charcount == 'on':
          analyzed = 0
          for char in fin:
               if not (char == " "):
                    analyzed=analyzed+1
          fin=fin+"-"+str(analyzed)
          purpose = purpose + "Char Counter"
          param = {'purpose': 'Char Counter', 'analyzed_text': analyzed}
          #return render(request, 'analyze.html', param)
     if newlineremover == "on":
          analyzed = ""
          for char in fin:
               if char != "\n" and char!="\r":
                    analyzed = analyzed+char
               param = {'purpose': 'New Line Remove', 'analyzed_text': analyzed}
          fin=analyzed
           #    return render(request, 'analyze.html', param)

     param={'purpose':purpose , 'analyzed_text' : fin}
     if removepunc == 'on' or fullcaps == 'on' or extraspaceremover=='on' or extraspaceremover == 'on' or newlineremover=='on':
          return render(request,'analyze.html',param)
     else:
          #analyzed = djtext
          #param = {'purpose': 'After Punctuation Remove', 'analyzed_text': analyzed}
          #return render(request,'analyze.html',param)
          return HttpResponse("error")




