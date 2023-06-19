from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    text =  """Lorem ipsum dolor sit amet, consectetur adipisicing elit. Numquam sit perspiciatis ipsa, nihil 
    omnis iure doloremque, voluptates incidunt reiciendis asperiores, ipsum minima illum provident earum iste
    eius inventore. Sint, fugiat?"""
    veg=['carrot','pumpkin','ladyfinger']
    p=[ {'name':'re1','age':15} ,{'name':'re3','age':18} ,{'name':'re5','age':19} ,{'name':'re7','age':17} ]
    return render(request,'index.html',context={'p':p,'text':text,'veg':veg})
    # return HttpResponse("<h1>bhai tu sahi jagah aya hai</h1>")
    # return HttpResponse("""<h1 style = "text-align: center";>bhai tu sahi jagah aya hai</h1>""")

def success_page(request):
    # return render(request,'index.html')
    return HttpResponse("<h1>you landed on my land</h1>")