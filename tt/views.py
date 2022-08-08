from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http  import HttpResponse
from .models import professor_subject as prof_subjec
from django.template import loader
def index(request):
    # template=loader.get_template('/index.html')
    return render(request,'index.html',{})
    
def professor_subject(request):
    return render(request,'professor-subject.html',{})

def student_register(request):
    prof_sub=prof_subjec.objects.all()
    su={'subjects':prof_sub}
    return render(request,'student-register.html',su)

@csrf_exempt

def prof_subj_registration(request):
    prof_na=request.Post.get('prof-name')
    subj_na=request.Post.get('subj-name')
    cred=request.Post.get('credits')
    # if(prof_nam)
    return render(request,'index.html')
