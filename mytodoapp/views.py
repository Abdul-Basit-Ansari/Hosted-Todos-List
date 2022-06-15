from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import todo
from django.contrib import messages
from django.contrib.auth  import authenticate,  login, logout
# Create your views here.
def index(request):
	user = request.user
	if user.is_authenticated:
		todos = todo.objects.filter(user=user).order_by('-time')
		dic ={'todos':todos,'user':user}
		return render(request,'index.html',dic)
	else:
		return render(request,'index.html')





def addtodo(request):
	user = request.user
	if user.is_authenticated:
		if request.method == "POST":
			title = request.POST.get('title')
			desc = request.POST.get('desc')

			todos=todo(title=title,desc=desc,user=user)
			todos.save()
			
	return redirect(index)









def signup(request):
	u=request.user
	if u.is_authenticated:
		return redirect("index")
	elif not u.is_authenticated :	
		if request.method == "POST":
			fname = request.POST.get('fname')
			lname = request.POST.get('lname')
			uname = request.POST.get('uname')
			phone = request.POST.get('phone')
			email = request.POST.get('email')
			pass1 = request.POST.get('pass1')
			pass2 = request.POST.get('pass2')
			# print(fname,lname,uname,phone,email,pass1,pass2)
			if pass1 != pass2 :
				messages.error(request,"Passwords Is Diffrent")
			user = 	User.objects.create_user(uname,email,pass1)
			user.first_name = fname
			user.last_name = lname

			user.save()
			login(request, user)
			messages.success(request,"Your Account Is Created")
			return redirect("index")
	print("signup")

	dic={'user':u}
	if not u.is_authenticated:
		return redirect("index",dic)
	if u.is_authenticated:
		return redirect("index")


def ulogin(request):
	user = request.user
	if request.method == "POST":
			uname=request.POST.get('uname')
			password=request.POST.get('password')
			user=authenticate(username= uname, password=password)
			print(uname,password)
			if user is not None:
				login(request, user)
				messages.success(request, "Successfully Logged In")
				dic={'user':request.user}
				if not user.is_authenticated:
					return redirect("index",dic)
				if user.is_authenticated:
					return redirect("index")



			else:
				messages.error(request, "Invalid credentials! Please try again")
				# return redirect("home")
	
	return redirect("index")



def ulogout(request):
	user = request.user
	logout(request)
	return redirect(index)


def udelete(request,sno):
	user = request.user
	item = todo.objects.get(sno=sno , user=user).delete()
	# item.delete()
	return redirect(index)