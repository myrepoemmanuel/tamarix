from http import client
import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import ClientDetails, PersonalProfile

# Create your views here.


def index(request):
    context = {}
    return render(request, 'blog/index.html', context)

def about(request):
    context = {}
    return render(request, 'blog/about.html', context)

def articles(request):
    context = {}
    return render(request, 'blog/articles.html', context)


def tamarix(request):
    context = {}
    return render(request, 'blog/tamarix.html', context)


def process_client(request):
    # transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    ClientDetails.objects.create(
        user=request.user,
        client_code=data['clientform']['Client_Code'],
        date_from=data['clientform']['from_date'],
        date_to=data['clientform']['to_date'],
        number_of_hours=data['clientform']['Number_of_hours'],
        number_of_session=data['clientform']['Number_of_session'],
        counselor_name=data['clientform']['Name_of_Counselor'],
        counselor_Association=data['clientform']['Association_No_Counselor'],
        counselor_Association_body=data['clientform']['Counselor_body'],
        supervisor_name=data['clientform']['Name_of_Supervisor'],
        supervisor_Association=data['clientform']['Association_No_Supervisor'],
        supervisor_Association_body=data['clientform']['Association_No_Supervisor'],
        presenting_problem=data['clientform']['client_problem'],
    )
    
    # client_user.save()


    return JsonResponse('client saved', safe=False)



def tamarix_preview(request,*args, **kwargs):
    print(kwargs)
    client_details = ClientDetails.objects.all()
    personal_details = PersonalProfile.objects.all()
    context = {'client_details':json.dumps(list(client_details.values())), 'personal_details':personal_details}
    return render(request, 'blog/tamarix_preview.html', context)

















