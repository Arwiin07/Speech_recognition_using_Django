from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import audioprocess,models
from django.contrib import messages


def index(request,*args,**kwargs):
    import pdb;pdb.set_trace()
    if request.user.username==request.POST.get("Uname"):
        return render(request,'second_page.html')
    else:
        return render(request, 'login.html')

# Create your views here.

def audio_process(request):
    print(request.POST)
    # import pdb;pdb.set_trace()
    audio_dir = "D:\Mchine learning_integration\Arwin\Speech_recognition\media" + "\\" + request.POST.get('filename')

    file_name1=request.POST.get('filename')
    # import pdb;pdb.set_trace()
    if models.Person.objects.filter(file_name=file_name1).exists():
        messages.error(request, "Error: File Already Transcripted,Choose Another File.")
        return render(request,"second_page.html")
    else:
        data_out = audioprocess.upload(audio_dir)
        transcript,out_score = audioprocess.speechrecog(data_out)
        print(transcript,'sdjkh')
    # import pdb;pdb.set_trace()
    # if models.Person.objects.filter(file_name=file_name1).exists():
        models.Person.objects.create(file_name=file_name1,transcripted_sentence=transcript,Sentiment_analysis=out_score)
        return render(request,'index.html',{'text_transcript':transcript,'score':out_score,'file_name':file_name1})

# Create your views here.

# def audio_process(request):
#     print(request.POST)
#     # import pdb;pdb.set_trace()
#     audio_dir = "D:\Mchine learning_integration\Arwin\Speech_recognition\media"+ "\\" + request.POST.get('filename')
#     file_name1=request.POST.get('filename')
#     # import pdb;pdb.set_trace()
#     if models.Person.objects.filter(file_name=file_name1).exists():
#         messages.error(request, "Error: File Already Exist,Choose Another File.")
#
#         return render(request,"second_page.html")
#     else:
#         data_out = audioprocess.upload(audio_dir)
#         transcript,out_score = audioprocess.speechrecog(data_out)
#         print(transcript,'sdjkh')
#     # import pdb;pdb.set_trace()
#     # if models.Person.objects.filter(file_name=file_name1).exists():
#         models.Person.objects.create(file_name=file_name1,transcripted_sentence=transcript,Sentiment_analysis=out_score)
#         return render(request,'index.html',{'text_transcript':transcript,'score':out_score,'file_name':file_name1})

# @login_required
def login(request):
    return render(request,"login.html")

def second_page(request):
    # import pdb;pdb.set_trace()
    return render(request,'second_page.html')


def choosing(request):
    if request.user.username==request.POST.get("Uname"):
        return render(request,'choosing.html')
    else:
        return render(request, 'login.html')
    # return render(request,'choosing.html')

def lists(request):
    lists_of_transcriptions=models.Person.objects.all()
    return render(request,"listing_db_elements.html",{'lists_of_transcripts':lists_of_transcriptions})


def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}
    # import pdb;pdb.set_trace()

    # add the dictionary during initialization
    context["data"] = models.Person.objects.get(id=id)

    return render(request, "detail_view.html", context)