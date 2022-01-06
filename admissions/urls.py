from django.urls import path

from admissions.views import addadmission;
from admissions.views import admissionReport;


urlpatterns = [

    path('newadm/',addadmission),
    path('admreporter/',admissionReport),

]
