from django.shortcuts import render,redirect
from .models import *


def register(request):
     return render(request,'register.html')

def login_page(request):
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