from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':1909,'b' : 2000, 'c' :3000 }
    return render(request,'conditions.html',context=d)



def loops (request):
    d={'name' : 'vinod'}
    return render(request,'loops.html',d)