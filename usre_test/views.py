from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def login(request):
    if request.method == 'POST':
        name = request.POST['username']
        passwd = request.POST['password']
        user = authenticate(username=name, password=passwd)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return redirect('/index/')
        else:
            return render(request, 'login.html', {'message': '登录失败'})
    else:
        return render(request, 'login.html')


def index(request):
    if request.user.is_authenticated:
        username = request.user.username
        return render(request, 'index.html', locals())
    return render(request, 'index.html')


@login_required(login_url='/login/')
def userinfo(request):
    if request.user.is_authenticated:
        username = request.user.username
        try:
            userinfo = User.objects.get(username=username)
        except:
            pass
    return render(request, 'userinfo.html', locals())


def logout(request):
    auth.logout(request)
    return redirect('/index/')

def email(request):
    # send_mail的参数分别是  邮件标题，邮件内容，发件箱(settings.py中设置过的那个)，收件箱列表(可以发送给多个人),失败静默(若发送失败，报错提示我们)
    send_mail('Subject here', 'Here is the message.', '17711046053@163.com',
              ['17711046053@163.com'], fail_silently=False)
    return render(request, 'email.html')