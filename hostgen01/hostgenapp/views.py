
from django.shortcuts import render

# Create your views here.
from hostgenapp.models import hosts
from hostgenapp.forms import api_host_gen, MyUserProfileForm, MyUserForm, generate_hosts_form

from hosts_generator import populate

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
   host_list = hosts.objects.order_by('h_ip')
   host_dict = {'hosts':host_list}
   return render(request,'hostgenapp/index.html',context=host_dict)

def api_list(request):
   api_list = hosts.objects.order_by('h_ip')
   api_dict = {'hosts':api_list}
   return render(request,'hostgenapp/api_list.html',context=api_dict)

def api_gen(request):
   form = api_host_gen()


   if request.method == 'POST':
      form = api_host_gen(request.POST)
      if form.is_valid():
         form.save(commit=True)
#         return index(request)
      else:
         print('Error.....')

   return render(request,'hostgenapp/api_gen.html',{'form':form})

def generate_hosts(request):
#    form = generate_hosts_form()
    generated = False
    form = generate_hosts_form()
    if request.method == 'POST':
        form = generate_hosts_form(request.POST)
        if form.is_valid():
            count = form.cleaned_data['no_hosts']
            populate(int(count))
            generated = True
#            return render(request,'hostgenapp/special.html')
        else:
            generate_hosts_form()
    print(generated)
    return render(request,'hostgenapp/generate_api.html',{'form':form})


@login_required
def special(request):
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = MyUserForm(data=request.POST)
        profile_form = MyUserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = MyUserForm()
        profile_form = MyUserProfileForm()

    return render(request,'hostgenapp/registeration.html',{'user_form':user_form,'profile_form':profile_form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('api_gen'))
            else:
                return HttpResponse("You account is not Active!")
        else:
            print("Someone tried to login and failed")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid ligin details supplied")
    else:
        return render(request,'hostgenapp/login.html',{})

