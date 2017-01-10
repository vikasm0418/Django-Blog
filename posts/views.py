from django.http import HttpResponse
from django.shortcuts import render

def post_create(request):

	return HttpResponse("<h1>Hello</h1>")

def post_detail(request):

	return HttpResponse("<h1>Hello</h1>")

def post_list(request):
	if request.user.is_authenticated():
		context = {
			"title" : "My User List"
		}
	else :
		context = {
			"title": " list"
		}
	return render(request,"index.html",context)

def post_update(request):

	return HttpResponse("<h1>Hello</h1>")

def post_delete(request):

	return HttpResponse("<h1>Hello</h1>")
