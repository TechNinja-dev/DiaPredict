from django.shortcuts import render
from django.http import request
from django.http import JsonResponse

from .model import predict
def home(request):
    return render(request,'home.html')
def evaluate(request):
# 'Gender', 'AGE', 'Urea', 'Cr', 'HbA1c', 'Chol', 'TG','HDL', 'LDL', 'VLDL', 'BMI']
    g=request.GET.get('Gender')
    if g=="Female":
        g=0
    elif g=="Male":
        g=1
    else:
        g=2
    a=request.GET.get("AGE")
    u=request.GET.get("Urea")
    cr=request.GET.get("Cr")
    hb=request.GET.get("HbA1c")
    ch=request.GET.get("Chol")
    tg=request.GET.get('TG')
    hdl=request.GET.get('HDL')
    ldl=request.GET.get('LDL')
    vldl=request.GET.get('VLDL')
    bmi=request.GET.get('BMI')
    print("hello")
    response=predict(g,a,u,cr,hb,ch,tg,hdl,ldl,vldl,bmi)
    response=int(response[0])
    rel=None
    if response==0:
        rel="Not a Diabetic"
    else:
        rel="Diabetic"
    return JsonResponse({"status":rel})
    # return HttpResponse("<h1> Evalute called</h1>")

    