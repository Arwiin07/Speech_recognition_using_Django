from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import audioprocess


def index(request,*args,**kwargs):
    # import pdb;pdb.set_trace()
    if request.user.username==request.POST.get("Uname"):
        return render(request,'index.html')
    else:
        return render(request, 'login.html')


# Create your views here.

def audio_process(request):
    print(request.POST)
    #import pdb;pdb.set_trace()
    audio_dir = "D:\Mchine learning_integration\Arwin\Speech_recognition\media"+ "\\" + request.POST.get('filename')

    data_out = audioprocess.upload(audio_dir)
    transcript,out_score = audioprocess.speechrecog(data_out)
    print(transcript,'sdjkh')




    return render(request,'index.html',{'text_transcript':transcript,'score':out_score})

# @login_required
def login(request):
    return render(request,"login.html")