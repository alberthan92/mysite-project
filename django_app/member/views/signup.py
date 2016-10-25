from django.shortcuts import render
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth import login as auth_login
from member.models import MyUser
from member.forms import SignupForm


def signup(request):
    nextsignup = request.GET.get('nextsignup')
    if request.method == 'POST':
        try:
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            nickname = request.POST['nickname']
            last_name = request.POST['last_name']
            first_name = request.POST['first_name']
            print(request.POST)
        except KeyError:
            return HttpResponse('email, password, nickname, last name or first name is invalid.')

        if password1 != password2:
            return HttpResponse('password is incorrect')

        new_user = MyUser.objects.create_user(
            email=email,
            password1=password1,
            password2=password2,
            nickname=nickname,
            last_name=last_name,
            first_name=first_name,
        )

        # posts = Post.objects \
        #     .filter(
        #     Q(published_date__lte=timezone.now()) |
        #     Q(published_date=None)
        # ).order_by('published_date')

        auth_login(request, new_user)
        messages.success(request, 'signup completed')
        return render(request, 'blog/post_list.html',{})
        # return render(request, 'blog/post_list.html',{'post_list': posts, 'title': '타이틀 변수는 title키를 이용해서 접근'})
    else:
        return render(request, 'member/signup.html',{})