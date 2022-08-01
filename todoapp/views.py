# by defalut
from ast import Delete
from django.shortcuts import redirect, render,HttpResponse
# django gives form(imported by me)
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login as loginpage,logout
from numpy import delete
from todoapp.forms import TODOform
from todoapp.models import Todo
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='signup')
def index(request):
    # return HttpResponse("hii")
    if request.user.is_authenticated:
        user=request.user
        form=TODOform()
        todos=Todo.objects.filter(user=user).order_by('priority')
        return render(request,'index.html',context={'form':form, 'todos':todos})

def login(request):
    if request.method == 'GET':

        form=AuthenticationForm()
        context={
            'form':form
        }
        return render(request,'login.html',context)
    else:
        form = AuthenticationForm(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            print('authenticate',user)
            if user is not None:
                loginpage(request,user)
                return redirect('home')
        else:
            context = {
                'form': form
            }
        return render(request, 'login.html', context)



def signup(request):

    if request.method=='GET':
    # django form
        form=UserCreationForm()
        context={
            'form':form
        }
        return render(request,'signup.html', context)

    else:
        form=UserCreationForm(request.POST)
        context = {
            'form': form
        }
        if form.is_valid():
            # return HttpResponse('form is valid')
            user=form.save()
            print(user)
            if user is not None:
                return redirect('login')

        else:
            # return HttpResponse("form is invalid")
            return render(request,'signup.html',context)



@login_required(login_url='login')
def addtodo(request):
    # to check user is exit
    if request.user.is_authenticated:
        user=request.user
        print(user)
        # if user is exit (registered or login already) then POST data
        form=TODOform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # save data
            todo=form.save(commit=False)
            todo.user=user
            todo.save()
            print(todo)
            return redirect("home")
        else:
            context={ 
                'form':form
            }
            return render(request,'index.html',context)


def signout(request):
    logout(request)
    return redirect('login')

def delete_todo(request,id):
    print(id)
    Todo.objects.get(pk = id).delete()
    return redirect('home')


def change_status(request,id,status):
    i=Todo.objects.get(pk=id)
    i.status = status
    i.save()
    return redirect('home')