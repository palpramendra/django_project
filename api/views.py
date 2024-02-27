
from django.http import JsonResponse
from apps.core.models import Category, Job, Contact, JobApplication

def category(request):
    category= Category.objects.get(id=5)
    return JsonResponse({
        "uuid": category.uuid,
        "created_at": category.created_at,
        "updated_at": category.updated_at,
        "title": category.title
    })

#  def category(request):
#     categories = Category.objects.all()
#     response = []
#     for category in categories:
#         response.append({
#             "uuid": category.uuid,
#             "created_at": category.created_at,
#             "updated_at": category.updated_at,
#             "title": category.title
#         })
#         return JsonResponse(response, safe=False)



def job(request):
    jobs = Job.objects.all()
    response = []
    for job in jobs:
        response.append({
            "uuid": job.uuid,
            "created_at": job.created_at,
            "updated_at": job.updated_at,
            "title": job.title,
            "application_deadline": job.application_deadline,
            "is_active": job.is_active,
            "category_id": job.category_id
        })
    return JsonResponse(response, safe=False)

def contact(request):
    contacts = Contact.objects.all()
    response = []
    for contact in contacts:
        response.append({
            "uuid": contact.uuid,
            "created_at": contact.created_at,
            "updated_at": contact.updated_at,
            "name": contact.name,
            "email": contact.email,
            "phone_number": contact.phone_number,
            "message": contact.message
        })
        return JsonResponse(response, safe=False)


def jobapplication(request):
    jobapplications = JobApplication.objects.all()
    response = []
    for jobapplication in jobapplications:
        response.append({
            "uuid": jobapplication.uuid,
            "created_at": jobapplication.created_at,
            "updated_at": jobapplication.updated_at,
            "interview_date": jobapplication.interview_date,
            "status": jobapplication.status,
            "job_id": jobapplication.job_id,
            "user_id": jobapplication.user_id

        })
        return JsonResponse(response, safe=False)
