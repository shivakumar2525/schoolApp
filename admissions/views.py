from django.shortcuts import render

# Create your views here.


#functions based
def homepage(request):
    return render(request,'index.html');


def addadmission(request):
    return render(request,'admissions/addadmission.html');

def admissionReport(request):
    return render(request,'admissions/admissionreport.html');
