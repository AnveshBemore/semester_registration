from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.http  import HttpResponse
from .models import professor_subject as prof_subjec
from .models import student
from django.template import loader
def index(request):
    # template=loader.get_template('/index.html')
    std=student.objects.all()
    a=[]
    n=0
    m=0
    for i in range(5):
        b=[]
        for j in range(10):
            for  k in std:
                if(m>=n):
                    c="course"+str(m)
                    b.append(j."course"+str(m))
            print(b)
        n+=1


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


@csrf_exempt
def student_registered(request):
    student.objects.all().delete()
    stdId=request.POST.get('std_id')
    stdName=request.POST.get('std_name')
    std=student(std_id=stdId,std_name=stdName)
    std.save()

    subj=prof_subjec.objects.all()

    stud=student.objects.get(std_id=stdId)
    c=1

    for i in subj:
        # prof[i.subj_name]=request.Post.get(i.subj_name)
        pname=request.POST.get(i.subj_name)
        s=i.subj_name
        # stdid=request.POST.get(s)
        id=(prof_subjec.objects.filter(Q(prof_name=pname)&Q(subj_name=s)         
        ))        
        # print(id.subj_name)
        for j in id:
            print(j.subj_name)
            profess_selected=j.prof_subj_id
            if(c==1):
                stud.course1=profess_selected
            elif(c==2):
                stud.course2=profess_selected
            elif(c==3):
                stud.course3=profess_selected
            elif(c==4):
                stud.course4=profess_selected
            elif(c==5):
                stud.course5=profess_selected
            elif(c==6):
                stud.course6=profess_selected
            elif(c==7):
                stud.course7=profess_selected
            elif(c==8):
                stud.course8=profess_selected

        print(id,"\n")
        c=c+1
    stud.save()
    return render(request,'index.html',{})