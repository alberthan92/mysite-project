from django.contrib import messages
from django.contrib.auth import authenticate as auth_authenticate
from django.contrib.auth import login as auth_login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from apis import facebook

__all__ = [
    'login',
    'login_facebook',
]

# @csrf_exempt
def login(request):
    next = request.GET.get('next')
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
        except KeyError:
            return HttpResponse('username 또는 password는 필수항목입니다')
        user = auth_authenticate(
            username=username,
            password=password
        )

        if user is not None:
            auth_login(request, user)
            messages.success(request, '로그인에 성공하셨습니다.')
            return redirect(next)
        else:
            messages.error(request, '로그인에 실패하였습니다.')
            return render(request, 'member/login.html', {})
    else:
        return render(request, 'member/login.html', {})



def login_facebook(request):
    if request.GET.get('error'):
        messages.error(request, 'failed login')
        return redirect('member:login')
    if request.GET.get('code'):
        REDIRECT_URI = 'http://127.0.0.1:8000/member/login/facebook/'
        code = request.GET.get('code')
        access_token = facebook.get_access_token(code, REDIRECT_URI)
        user_id = facebook.debug_token(access_token)
        user_info = facebook.get_user_info(user_id, access_token)


        #authenticate backends
        dict_user_info = facebook.get_user_info(user_id, access_token)
        user = auth_authenticate(user_info=dict_user_info)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Facebook login success')
            return redirect('blog:post_list')
        else:
            messages.error(request, 'Failed Facebook login')
            return redirect('member:login')