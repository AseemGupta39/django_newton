from django.shortcuts import render,redirect
from .models import *
import os
     
# Create your views here.
def receipes(request):
     if request.method == "POST":
          data = request.POST
          receipe_image = request.FILES.get('receipe_image')
          pdf1.objects.create(receipe_image=receipe_image)
          if str(receipe_image).endswith('.pdf'):
               print("submitted")
               from pdf2docx import Converter
               # C:\Users\ASEEM\Documents\test\django_newton\public\static\pdf_fol\OOPS_in_Java.pdf
               pdf_file = os.path.join('C:\\Users\\ASEEM\\Documents\\test\\django_newton\\public\\static\\pdf_fol',str(receipe_image))
               docx_name=str(receipe_image).replace('pdf','docx')
               docx_file = os.path.join('C:\\Users\\ASEEM\\Documents\\test\\django_newton\\public\\static\\pdf_fol',str(docx_name))
               
               # docx_file = os.path.join(docx_name)


# convert pdf to docx
               cv = Converter(pdf_file)
               cv.convert(docx_file)      # all pages by default
               cv.close()
               context={'file': os.path.abspath(docx_file)}
               print(f"downloadind {os.path.abspath(docx_file)}")
               return render(request,'pd.html',context)
     
     queryset = pdf1.objects.all()
     
     context = {'receipes':queryset}   
 
     return render(request,"recepies.html",context)

# /media/{{receipe.receipe_image}}