# Create your views here.
from newsreader.nread.models import *
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response,redirect
@csrf_exempt
def feed_list(request):
	flist=feed.objects.filter()
	flist=flist.order_by('-date')
	for f in flist:
		f.description=' '.join(f.description.split(' ')[0:5]).encode()
	return render_to_response('newsreader/temp/feed_list.html',{'l':flist})
	pass
@csrf_exempt
def view_feed(request):
	name=request.POST.get('feed_id')
	a=feed.objects.get(id=name)
	return render_to_response('newsreader/temp/view_feed.html',{'view':a})
	pass
@csrf_exempt
def save(request):
	feed_id=request.POST.get('feed_id')
	cont=request.POST.get('file_content')
	f=feed.objects.filter(id=feed_id)
	f.update(description=cont)
	flist=feed.objects.filter()
	flist=flist.order_by('-date')
	for d in flist:
		d.description=' '.join(d.description.split(' ')[0:5]).encode()
	return render_to_response('newsreader/temp/feed_list.html',{'l':flist})
	pass
@csrf_exempt
def annotate(request):
	feed_id=request.POST.get('feed_id')
	cont=request.POST.get('file_content')
	a=feed.objects.filter(id=feed_id)
	a.update(description=cont)	
	return render_to_response('newsreader/temp/annotate.html',{'view':a[0]})
	pass