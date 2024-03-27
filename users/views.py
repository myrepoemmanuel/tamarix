import json
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from .models import Profile

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} created successfully')
            return redirect('site-login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})



def mylogin(request):
    logout(request)
    username=password= ""

    if request.method == 'POST':
        # print(request.POST)
        username=request.POST['username']
        password=request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('site-profile')
        else:
            return redirect('site-login')
    context = {}
    return render(request, 'users/login.html')



@login_required
def profile(request):

    profile = Profile.objects.filter(user=request.user).values()[0]

 
    for key, value in profile.items():
        if value == None:
            profile[key] = ""
    
        
    context = {"profile":profile,"username":request.user}
    return render(request, 'users/profile.html', context)

def process_profile(request):
    # transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    profile = Profile.objects.get(user=request.user)
    
    profile.first_name=data['profileInfo']['first_name']
    profile.last_name=data['profileInfo']['last_name']
    profile.phone=data['profileInfo']['phone']
    profile.address_one=data['profileInfo']['address_1']
    profile.address_two=data['profileInfo']['address_2']
    profile.postcode=data['profileInfo']['postalcode']
    profile.country=data['profileInfo']['country']
    profile.region=data['profileInfo']['region']
    
    
    profile.save()


    return JsonResponse('profile saved', safe=False)



