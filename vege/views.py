from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def register(request):
     if request.method == "POST":
          data = request.POST
          first_name= data.get('first_name')
          last_name = data.get('last_name')
          username =  data.get('username')
          password =  data.get('password') 

          user = User.objects.filter(username=username)
          
          if user.exists():
               messages.error(request, "username already exist.")
               return redirect('/register/')

          print("\n\n\n\n",first_name,last_name,username,password,"\n\n\n\n")

          user = User.objects.create(
               first_name=first_name,
               last_name=last_name,
               username=username
          )
          
          user.set_password(password)
          user.save()
          messages.success(request, "account registerd.")
          return redirect("/login/")

     return render(request,'register.html')


def logout_page(request):
     logout(request)
     return redirect('/login/')


def login_page(request):
     if request.method == "POST":
          data = request.POST
          username =  data.get('username')
          password =  data.get('password') 

          if not User.objects.filter(username=username).exists():
               messages.error(request, "Invalid username")
               return redirect('/login/')
          
          user = authenticate(username=username,password=password)
          
          if user is None:
               messages.error(request,"invalid password")
               return redirect('/login/')

          else:
               # messages.success(request,"logged in")
               login(request,user=user)
               return redirect('/receipes/')
          # return redirect('/login/')
          
          

     return render(request,'login.html')

def update_receipe(request,id):
     queryset = Recepie.objects.get(id=id)
     
     if request.method == "POST":
          data = request.POST
          receipe_image = request.FILES.get('receipe_image')
          receipe_name = data.get("receipe_name")
          receipe_description = data.get("receipe_description")

          queryset.receipe_name = receipe_name
          queryset.receipe_description = receipe_description

          if receipe_image:
               queryset.receipe_image = receipe_image
          
          queryset.save()
          return redirect('/receipes/')

     context = {'receipe':queryset}   
     return render(request,"update_recepies.html",context)



def delete_receipe(request,id):
     # if request.method == "POST":
     queryset = Recepie.objects.get(id=id)
     queryset.delete()
     print(f"deleted {id}")
     return redirect('/receipes/')

     
# Create your views here.
@login_required(login_url='/login/')
def receipes(request):
     if request.method == "POST":
          data = request.POST
          receipe_image = request.FILES.get('receipe_image')
          receipe_name = data.get("receipe_name")
          receipe_description = data.get("receipe_description")
          # print(receipe_name,receipe_description,receipe_image)
          Recepie.objects.create(receipe_name=receipe_name,
                                 receipe_description=receipe_description,
                                 receipe_image=receipe_image)
          
          return redirect('/receipes/')
     
     queryset = Recepie.objects.all()

     if request.GET.get('search'):
          print(request.GET.get('search'))
          queryset = queryset.filter(receipe_name__icontains=request.GET.get('search'))
     
     
     context = {'receipes':queryset}   
 
     return render(request,"recepies.html",context)

def get_students(request):
     queryset = Student.objects.all()
     paginator = Paginator(queryset, 25)  # Show 25 contacts per page.

     page_number = request.GET.get("page",1)
     page_obj = paginator.get_page(page_number)
     print(page_obj.object_list)
     return render(request,'report//students.html',{'queryset':page_obj})