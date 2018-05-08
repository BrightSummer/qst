from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
#  第四个是 auth中用户权限有关的类。auth可以设置每个用户的权限。

from .forms import UserForm


#  Create your views here.


# 注册
def register_view(req):
    context = {}
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            # 获得表单数据
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            #  判断用户是否存在
            user = auth.authenticate(username=username, password=password)
            if user:
                context['userExit'] = True
                return render(req, 'register.html', context)

            # 添加到数据库（还可以加一些字段的处理）
            user = User.objects.create_user(username=username, password=password)
            user.save()

            # 添加到session
            req.session['username'] = username
            # 调用auth登录
            auth.login(req, user)
            # 重定向到首页
            return redirect('/accounts/login/')
    else:
        context = {'isLogin': False}
    #  将req 、页面 、以及context{}（要传入html文件中的内容包含在字典里）返回
    return render(req, 'register.html', context)


# 登陆
def login_view(req):
    context = {}
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            # 获取表单用户密码
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # 获取的表单数据与数据库进行比较
            user = authenticate(username=username, password=password)
            if user:
                # 比较成功，跳转index
                auth.login(req, user)
                req.session['username'] = username
                return redirect('/card/')
            else:
                # 比较失败，还在login
                context = {'isLogin': False, 'pawd': False}
                return render(req, 'login.html', context)
    else:
        context = {'isLogin': False, 'pswd': True}
    return render(req, 'login.html', context)


# 登出
def logout_view(req):
    # 清理cookie里保存username
    auth.logout(req)
    return redirect('/')

#  def acc_login(request):
#      if request.method == "POST":
#          uname = request.POST.get("username", None)
#          print(uname)
#          pwd = request.POST.get("password", None)
#          print(pwd)
#          user = authenticate(username=uname, password=pwd)
#          print(user)
#          if user:
#              login(request, user)  #  验证成功之后登录
#              return redirect('/card')
#      return render(request, "login.html")
# 
# 
#  def acc_register(request):
#      if request.method == "POST":
#          username = request.POST.get("username", None)
#          password = request.POST.get("password", None)
#          User.objects.create_user(username=username, password=password)
#      return render(request, "register.html")
# 
# 
#  def acc_logout(request):
#      logout(request)  #  登出
# 
#      return redirect("/login")
