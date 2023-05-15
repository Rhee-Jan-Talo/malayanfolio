from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from profiles.models import *
from django.db.models import Q
from profiles.models import Documents



def Home(request):
    AllUsers = UserProfile.objects.all()
    userProfile = get_userProfile(request)
    context={
        'userProfile':userProfile,
        'AllUsers':AllUsers
    }
    return render(request, "home.html", context)


def ViewProfile(request, user_id):
    if request.user.is_authenticated:
        loggedInProfile = UserProfile.objects.get(user_id = request.user.id)
    else:
        loggedInProfile = None
    
    userProfile = UserProfile.objects.get(id=user_id)
    userOutputs = Outputs.objects.get(user_id = userProfile.id)
    userClubs = Clubs.objects.filter(user_id = userProfile.id)
    userLanguages = Languages.objects.filter(user_id = userProfile.id)
    userInterests = Interests.objects.filter(user_id = userProfile.id)
    userEducation = Education.objects.filter(user_id = userProfile.id)
    context={
        'UserProfile' : userProfile,
        'userOutputs':userOutputs,
        'userClubs':userClubs,
        'userLanguages':userLanguages,
        'userInterests':userInterests,
        'userEducation':userEducation,
        'userProfile':loggedInProfile
    }
    return render(request, 'profile.html', context)

def ProfileSearch(request):
    AllUsers = UserProfile.objects.filter(Q(lname__contains = request.POST['search_value']) | Q(fname__contains = request.POST['search_value']))
    userProfile = get_userProfile(request)
    context={
        'userProfile':userProfile,
        'AllUsers':AllUsers
    }

    return render(request, 'home.html', context)


def get_userProfile(request):
    if request.user.is_authenticated:
        userProfile = UserProfile.objects.get(user_id = request.user.id)
    else:
        userProfile = None
    return userProfile


def ViewDocuments(request, file_type, user_id):
    Profile = UserProfile.objects.get(id=user_id)
    docu_data = Documents.objects.filter(user_id = user_id).filter(folder_type=file_type).order_by("-id")
    context = {
        'docu_data': docu_data,
        'userProfile': Profile,
        'file_type': file_type,
    }
    return render(request, 'user_documents.html', context)


def handler404(request, *args, **argv):
    return render(request, 'errors/404.html', {})


def handler500(request, *args, **argv):
    return render(request, 'errors/404.html', {})



