from django.urls import path
from .views import category, job, contact, jobapplication

urlpatterns = [
    path('job-category/', category),
    path('job/', job),
    path('contact/', contact),
    path('jobapplication/', jobapplication)


]

