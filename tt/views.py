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
    # n=0
    # m=0
    # for i in range(5):
    #     b=[]
    #     for j in range(10):
    #         for  k in std:
    #             if(m>=n):
    #                 c="course"+str(m)
    #                 # b.append(j."course"+str(m))
    #         print(b)
    #     n+=1
    # for st in std:
    #     a.append(st.course1)
    #     a.append(st.course2)
    #     a.append(st.course3)
    #     a.append(st.course4)
    #     a.append(st.course5)
    #     a.append(st.course6)
    #     a.append(st.course7)
    #     a.append(st.course8)   


    return render(request,'index.html',{'a':std})
    
def professor_subject(request):
    return render(request,'professor-subject.html',{})

def student_register(request):
    prof_sub=prof_subjec.objects.all()
    su={'subjects':prof_sub}
    return render(request,'student-register.html',su)

@csrf_exempt

def prof_subj_registration(request):
    if request.method=="POST":
        prof_na=request.POST.get('prof-name')
        subj_na=request.POST.get('subj-name')
        cred=request.POST.get('credits')
        # if(prof_nam)
        profid=subj_na+"  Prof ."+prof_na
        prof=prof_subjec(prof_subj_id=profid,prof_name=prof_na,subj_name=subj_na,credits=cred)
        prof.save()
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

def hall_view(request):
    a={"h1":"hall 1","h2":"hall 2","h3":"hall 3","h4":"hall 4","h5":"hall 5"}
    b=["hall 1","hall 2","hall 3","hall 4"]
    c=["hall 5","hall 1","hall 2","hall 3"]
    days=["Monday","Tuesday","Wednesday","Thursday","Friday"]
    return render(request,'hall.html',{
        "a":b,"c":c,"days":days})


def prof_view(request):
    prof=prof_subjec.objects.all()
    a=[]
    for i in prof:
        a.append(i.prof_subj_id)
        print(i.prof_subj_id)
    std=student.objects.all()
    return render(request,'prof_view.html',{"a":a,"std":std,"h":"hello"})