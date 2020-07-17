from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
#User views

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'account created for {username}! Login to your account.')
            return redirect('login')
        else:
            messages.warning(request, f'please fill valid info!')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html',{'form':form})

#message.success
#message.warning
#message.info
#message.debug
#message.error
