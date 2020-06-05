from django.shortcuts import render

def home(request):
    username = request.POST.get('usr')
    password = request.POST.get('pass')
    print("Username is :",username)
    print("Password is :",password)

    return render(request,'home.html')