from django.shortcuts import render,redirect,HttpResponse
from .forms import StudentForm

from .models import StudentModel

# Create your views here.
def show_view(request):
    data=StudentModel.objects.all()
    return render(request,'view.html',{'data':data})

def create_data(request):
    if request.method=='POST':
        form=StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse("<h1>Form Submitted</h1>")
    return render(request,'create.html')

def update_data(request,id):
    data=StudentModel.objects.get(id=id)
    form=StudentForm(instance=data)
    if request.method=='POST':
        form=StudentForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save(commit=True)
            return redirect('show_view')  
    return render(request,'update.html',{'form ':form}) 
