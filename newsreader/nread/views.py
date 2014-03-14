# Create your views here.
from newsreader.nread.models import *
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
def feed_list(request):
	flist=feed.objects.filter()
	# flist=flist.order_by('-date')
	for f in flist:
		# b.append(' '.join(f.description.split(' ')[0:5]).encode())
		f.description=' '.join(f.description.split(' ')[0:5]).encode()
	return render_to_response('newsreader/temp/feed_list.html',{'l':flist})
	pass
def view_feed(request,name):
	a=feed.objects.get(id=name)
	return render_to_response('newsreader/temp/view_feed.html',{'view':a})
	pass
@csrf_exempt
def save(request):
	feed_id=request.POST.get('feed_id')
	cont=request.POST.get('file_content')
	f=feed.objects.get(id=feed_id)
	f.description=cont
	f.save()
	return render_to_response('newsreader/temp/save.html',{'f':cont})
	pass