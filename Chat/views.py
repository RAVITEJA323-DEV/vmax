from django.shortcuts import render,redirect
from .forms import *
from .models import * 
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView, DestroyAPIView
from rest_framework import mixins
from rest_framework.views import APIView
from .serializers import *
from .forms import CommentForm 
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
# Create your views here.

  
def post_detailview(request):
	cf = CommentForm()
	if request.method == 'POST': 
		cf = CommentForm(request.POST or None)
		if cf.is_valid(): 
			content = request.POST.get('content') 
			post = cf.cleaned_data.get('post')
			opinion = cf.cleaned_data.get('opinion')
			comment = Comment.objects.create(post= post, content = content, opinion= opinion) 
			comment.save() 
			redirect('post') 
		else: 
			cf = CommentForm()
	return render(request, 'Chat/post_detail.html', { 
      'comment_form':cf, 
      } )


def post_view(request):
	form =PostForm()
	if request.method == 'POST':
		form = PostForm(request.POST or None)
		if form.is_valid():
			form.save()
			return redirect('comment')
	return render(request, 'Chat/post_view.html', {'form':form })	



@receiver(post_save, sender=post_view)
def create_comment(sender, instance=None, created=False, **kwargs):
    if created:
        comment.objects.create(user=instance)


def home(request):
		if request.method=='POST':
			username = request.POST['username']
			password =request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('comment')
		return render(request, 'home.html')
	






class post_max(mixins.CreateModelMixin,
	       mixins.UpdateModelMixin,
	       mixins.DestroyModelMixin,
	       mixins.RetrieveModelMixin,
	       ListAPIView):
	       queryset=Comment.objects.all()
	       serializer_class=Custom_Serializer
	       def put(self,request,*args,**kwargs):
	       	return self.update(request,*args,**kwargs)

	       def patch(self,request,*args,**kwargs):
	       	return self.update(request,*args,**kwargs)

	       def Delete (self,request,*args,**kwargs):
	       	return self.destroy(request,*args,**kwargs)

	       def post(self,request,*args,**kwargs):
	       	return self.create(request,*args,**kwargs)


@login_required(login_url='home')
def display(request):
	if request.method=='GET':
		queryset = Comment.objects.all()

	return render(request, 'details.html', {'queryset':queryset})



class detailsapi(APIView):
	def get(self, request, format=None):
		comment = Comment.objects.all()
		serializer = Custom_Serializer(comment, many=True)
		return Response(serializer.data)