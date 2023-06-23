from django.shortcuts import render, redirect  #importing all the modules required to build the app
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import todo
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):                #created the home page
    if request.method == 'POST':  #POST method is used to send the data entered by the user to the backend
        #taking input from the user in the form
        task = request.POST.get('task')
        new_todo = todo(user=request.user, todo_name=task) #forming new todo list
        new_todo.save()

    all_todos = todo.objects.filter(user=request.user)  #filter all todo item from the database and give todo items created by the current logged in user
    #creating context to display it on frontend
    context = {
        'todos': all_todos
    }
    return render(request, 'todoapp/todo.html', context)  #takes you to the todo.html file inside the todoapp folder

def register(request):
    if request.user.is_authenticated: #checks if the user is authenticated(with a valid user account on the computer)
        return redirect('home-page')
    if request.method == 'POST':  #POST method is used to send the data entered by the user to the backend
        #taking input from the user in the form  
        username = request.POST.get('username')  
        email = request.POST.get('email')
        password = request.POST.get('password')

        if len(password) < 3:  #if the length of name is too short then throw error
            messages.error(request, 'Password must be at least 3 characters')
            return redirect('register')

        get_all_users_by_username = User.objects.filter(username=username)  #if the username already present in the database then throw error
        if get_all_users_by_username:
            messages.error(request, 'Error, username already exists, User another.')
            return redirect('register')

        new_user = User.objects.create_user(username=username, email=email, password=password)  #taking details from new user
        new_user.save()

        messages.success(request, 'User successfully created, login now') #throw message once the user has registered and redirect to the login page
        return redirect('login')
    return render(request, 'todoapp/register.html', {})

def LogoutView(request): #when user clicks on logout then redirect to login page
    logout(request)
    return redirect('login')

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    if request.method == 'POST':          #POST method is used to send the data entered by the user to the backend
        #taking details from user
        username = request.POST.get('uname')
        password = request.POST.get('pass')

        validate_user = authenticate(username=username, password=password) #checks if the user details are present in the database or not
        if validate_user is not None:
            login(request, validate_user)
            return redirect('home-page')
        else:
            messages.error(request, 'Error, wrong user details or user does not exist')
            return redirect('login')


    return render(request, 'todoapp/login.html', {})

@login_required
def DeleteTask(request, name):  #deletes the task
    get_todo = todo.objects.get(user=request.user, todo_name=name)
    get_todo.delete()
    return redirect('home-page')

@login_required
def Update(request, name):  #updates the task
    get_todo = todo.objects.get(user=request.user, todo_name=name)
    get_todo.status = True
    get_todo.save()
    return redirect('home-page')