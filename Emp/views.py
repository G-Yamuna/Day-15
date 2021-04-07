from django.shortcuts import render,redirect
from Emp.models import UsrRg,NewData
from Emp.forms import UsregForm,UserUpdate,NewUsrForm
from django.http import HttpResponse
# Create your views here.
def home(request):
	return render(request,'html/home.html')

def about(r):
	return render(r,'html/about.html')

def contact(r):
	return render(r,'html/contactus.html')

def login(r):
	return render(r,'html/login.html')

def register(r):
	if r.method == "POST":
		u=r.POST['uname']
		e=r.POST['eml']
		p=r.POST['ps']
		a=r.POST['aag']
		d={'user':u,'email':e,'pass':p,'age':a}
		return render(r,'html/details.html',{'d':d})
	return render(r,'html/register.html')

def crud(request):
	if request.method=="POST":
		un=request.POST['username']
		email=request.POST['email']
		pas=request.POST['password']
		age=request.POST['age']	
		data2=UsrRg.objects.all()
		if len(un)!=0:
			data=UsrRg.objects.create(username=un,password=pas,email=email,age=age)

		return render(request,'html/actions.html',{'info':data2})
		
	data2=UsrRg.objects.all()
	return render(request,'html/actions.html',{'info':data2})


def deletedata(req,id):
	data=UsrRg.objects.get(id=id)
	data.delete()
	return redirect('/cr')

def dform(request):
	if request.method == "POST":
		e=UsregForm(request.POST)
		if e.is_valid():
			q=e.save()
			y=NewData.objects.create(pid_id=q.id)
			# return HttpResponse("User Created Successfully")
			return redirect('/show')
	e=UsregForm()
	return render(request,'html/dyform.html',{'tu':e})	

def showinfo(re):
	data=UsrRg.objects.all()
	return render(re,'html/showdata.html',{'info':data})

def infodelete(re,id):
	data=UsrRg.objects.get(id=id)
	if re.method=="POST":
		data.delete()
		return redirect('/showdata')
	return render(re,'html/userdata.html',{'sd':data})

def edit(r,id):
	data=UsrRg.objects.get(id=id)
	if r.method=="POST":
		data.username=r.POST['username']
		data.age=r.POST['age']
		data.email=r.POST['email']
		data.password=r.POST['password']
		data.save()
		return HttpResponse("data saved")
	return render(r,'html/useredit.html',{'in':data})

def userupdate(m,si):
	t=UsrRg.objects.get(id=si)
	y=NewData.objects.get(pid_id=si)
	if m.method=="POST":
		d=UserUpdate(m.POST,instance=t)
		k=NewUsrForm(m.POST,instance=y)
		if d.is_valid() and k.is_valid():
			d.save()
			k.save()
			return redirect('/showdata')
	d=UserUpdate(instance=t)
	k=NewUsrForm(instance=y)
	return render(m,'html/updateuser.html',{'us':d,'nt':k})

def userinfo(r,uname):
	p=UsrRg.objects.get(username=uname)
	h=NewData.objects.get(pid_id=p.id)
	return render(r,'html/viewinfo.html',{'y':p,'yu':h})