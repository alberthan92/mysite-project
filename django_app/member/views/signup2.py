from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib import messages
from member.forms import SignupForm
from member.models import MyUser
def signup2(request):
    context = {}
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            last_name = form.cleaned_data['last_name']
            first_name = form.cleaned_data['first_name']
            nickname = form.cleaned_data['nickname']

            if password1 != password2:
                return HttpResponse('Password incorrect')

            user = MyUser.objects.create_user(
                email=email,
                last_name=last_name,
                first_nmae=first_name,
                nickname=nickname,
                password=password1,
            )

            login(request, user)
            messages.info(request, 'signup successful')
            return redirect('blog:post_list')




        else:
            context['form'] = form

    else:
        form = SignupForm()
        context['form'] = form
        return render(request, 'member/signup2.html', context)