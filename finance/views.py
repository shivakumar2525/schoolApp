from django.shortcuts import render

# Create your views here.


def feeCollection(request):
    return render(request,'finance/feecollection.html');

def feeDuesReport(request):
    return render(request,'finance/feeduesReport.html');

def feeCollectionReport(request):
    return render(request,'finance/feeCollectionReport.html');
    