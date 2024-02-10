from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout


def INDEX(request):
    return render(request, 'chat/index.html')
def LOGIN(request):
    return render(request, 'chat/login.html')

def LOGOUT(request):
    logout(request)
    return redirect('login')
