from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.template import loader
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from .models import User, UserWallet
import datetime
import random
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from za_id_number.za_id_number import (
  SouthAfricanIdentityValidate, SouthAfricanIdentityNumber)

from ._redoing import validate_password, create_username
from django.db.models import Q

from .forms import NewUserForm, ChangePwdForm

# Check for users that took 12months without login and Delete the account 
try:
  nw = datetime.date.today().month
  for i in User.objects.all():
    if nw - i.last_login.month == 12:
      if i.is_superuser is False or i.is_staff is False:
        i.delete()
except:
  False


class LaunchView(View):
  def get(self, request):
    form = NewUserForm()
    return render(
       request,
      '_users/_index.html',
     {
        'form': form
     }
    )

  def post(self, request):
    form = NewUserForm(request.POST)
    za_id_number = form['za_id_number'].value()
    first_name = form['first_name'].value()
    last_name = form['last_name'].value()
    if SouthAfricanIdentityValidate(za_id_number).valid:
        if SouthAfricanIdentityNumber(za_id_number).age >= 18:
            _user =  User.objects.filter(
                za_id_number=za_id_number,
                is_active=True,
                is_staff=False,
                is_superuser=False
            )
            if not _user:
                if form.is_valid():
                    username = create_username(first_name, last_name, User)
                    form.instance.username = username
                    form.save()
                    psw = form.cleaned_data['password1']
                    user = authenticate(
                        request, username=username, password=psw
                    )
                    if user.is_authenticated:
                        login(request, user)
                        messages.success(request, f'Wellcome to _green {first_name.capitalize()}') # return 
            else: messages.info(request, f'Hi {first_name.capitalize()} {last_name.capitalize()} you already have an Account')
        else: messages.warning(request, 'You must be 18 or older to register')
    else: messages.warning(request, 'Invalid ZA/RSA ID number')
    return render(
       request,
      '_users/_index.html',
     {
        'form': form
     }
	)

def login_index(request):
    context = {}
    return render(request, '_users/_login.html', context)

def login_user(request):
   pass
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         try:
#             user = authenticate(request, username=username, password=password)
#             if user.is_authenticated:
#                 if user.is_superuser == True:
#                     login(request, user)
#                     return HttpResponseRedirect(reverse('_fundraiser:admin-index'))
#                 elif user.is_staff == True:
#                     login(request, user)
#                     #return HttpResponseRedirect(reverse(''))
#                 elif user:
#                     login(request, user)
#                     return HttpResponseRedirect(reverse('_fundraiser:account-index'))
#         except:
#             invalid = True
#             return render(
#                 request,
#                 'login_.html',
#                 {
#                     'login_context': invalid,
#                 },
#             )
#     return HttpResponseRedirect(reverse('_splash:splash-view'))

# Logout user
def logout_view(request):
  logout(request)
  i = 'Logged Out'
  messages.info(request, f'{ i }')
  return HttpResponseRedirect(reverse('_users:index'))

# def chg_pwd(request):
#     form = ChangePwdForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'chg_pwd_.html', context)

# # Change password
# def change_password(request):
#     if request.method == 'POST':
#         form = ChangePwdForm(request.POST)
#         _usename = request.POST['username']
#         _zaID = request.POST['za_id_number']
#         _password = request.POST['create_password']
#         _confirmPwd = request.POST['confirm_password']
#         if validate_password(request.POST['create_password']) == True:
#             if _password == _confirmPwd:
#                 if NewUser.objects.filter(username=_usename, za_id_number=_zaID).exists():
#                     _user = NewUser.objects.filter(username=_usename).get()
#                     new_password = _password
#                     _user.set_password(new_password)
#                     _user.save()
#                     messages.success(request, 'Password has been successfully changed')
#                 else:
#                     messages.warning(request, 'Invalid username/za_id_number')
#                     context = {'form': form}
#                     return render(request, 'chg_pwd_.html', context)
#             else:
#                 messages.warning(request, 'Passwords don\'t match')
#                 context = { 'form': form}
#                 return render(request, 'chg_pwd_.html', context)
#         else:
#             messages.warning(request, f'{validate_password(_password)}')
#             context = {'form': form}
#             return render(request, 'chg_pwd_.html', context)
#     return HttpResponseRedirect(reverse('_splash:chgpwd-index'))
