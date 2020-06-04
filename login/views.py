from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login as djangoLogin,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
	if request.user.is_authenticated:
		return redirect('/posts')
	else:
		if request.method=="POST":
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				djangoLogin(request,user)
				return redirect('/posts/')
			else:
				messages.info(request , 'Invalid Credentails')
		return render(request, 'login/loginpage.html')

def signup(request):
	if request.user.is_authenticated:
		return redirect('/posts')
	else:
		form=CreateUserForm()
		if request.method=="POST":
			form=CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				username = form.cleaned_data.get('username')
				messages.success(request,"Accont Created for "+username)
				return redirect('/login')
		context={'form':form}
		return render(request,'login/signup.html',context)

def userlist(request):
	user_list = User.objects.all()
	return render(request,'login/userList.html',{'users':user_list}) #passing query to template

def post_feed(request):
	posts = Post.objects.order_by('-date_posted') #Sorts the post by most recent first
	return render(request,'login/posts.html',{'posts':posts})

def profile(request,userid):
	user = User.objects.get(id=userid)
	posts = user.post_set.all()
	return render(request,'login/profilepage.html',{'user':user,'posts':posts})

@login_required(login_url='login')
def postForm(request):
	if request.method == 'POST':
		form = CreatePostForm(request.POST)
		print(form)
		if form.is_valid():
			form.save()
			return redirect('/posts')
	return render(request,'login/Postform.html',{'form':CreatePostForm(initial={'user':request.user.user}),'user':user})

@login_required(login_url="login/")
def editPostForm(request,id):
	currentPost = Post.objects.get(id=id)
	if request.method == 'POST':
		form = CreatePostForm(request.POST,instance=currentPost)
		if form.is_valid():
			form.save()	
	return render(request,'login/Postform.html',{'form':CreatePostForm(instance=currentPost)})

@login_required(login_url="login/")
def deletePostForm(request,id):
	currentPost = Post.objects.get(id=id)
	if request.method == 'POST':
		currentPost.delete()
		return redirect('/posts')
	return render(request,'login/deletePost.html',{'post':currentPost})

@login_required(login_url="login/")
def logoutPage(request):
	logout(request)
	return redirect('/')
