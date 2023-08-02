from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from store.forms import CustomUserForm

def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered Successful!! Login To Proceed")
            return redirect('/login')
    context = {'form':form}
    return render(request, "store/auth/register.html", context)

def loginpage(request):
    if request.user.is_authenticated:
         messages.warning(request, " You are already loggedin")
         return redirect("/")
    else:
     if request.method == 'POST':
        name = request.POST.get('UserName')
        Password = request.POST.get('Password')

        user = authenticate(request, username=name, password=Password)

        if user is not  None:
            login(request, user)
            messages.success(request, "Logged in successful")
            return redirect("/")
        else:
            messages.error(request, "Invailid ID or Password")
            return redirect('/login')
     return render(request, "store/auth/login.html" )
    
def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logout in successful")
    return redirect("/")
    
    