from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

from django.contrib.auth.models import User
from .forms import SignUpForm



def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')

            #create the User
            user = User.objects.create_user(username = username,
                                 email = email,
                                 password = raw_password)

            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            # redirect user to home page
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})