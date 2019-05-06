from django.shortcuts import render
# from first_app.models import info
from first_app.forms import newuserform
# Create your views here.
def index(request):
    return render(request,"first_app/index.html")
def index1(request):
    form = newuserform()

    if request.method=='POST':
        form = newuserform(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else :
            print('error')
    return render(request,'first_app/first_appuser.html',{'form':form})
