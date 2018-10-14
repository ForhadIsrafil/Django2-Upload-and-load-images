from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import Pic
import mimetypes # for findout the file types/extensions

def get_pic(request):
	pics               = Pic.objects.all().order_by('-id')
	if request.method == 'POST': #and request.FILES['image']
		try:
			im         = request.FILES['image']
			print(im)
			file_type  = mimetypes.guess_type(str(im),strict=False) #strict=True,then it support txt,html,xml format
			print(file_type[0])
			extensions = ['image/gif', 'image/jpeg', 'image/png']
			if file_type[0] in extensions:
				save   = Pic(i=im)
				save.save()
				return redirect('/')
			else:
				return HttpResponse('<h2>Sorry the file format is not supported!</h2>')
		except Exception:
			return HttpResponse('<h2>Sorry file not selected!</h2>')
	return render(request, 'upload.html',{'pics': pics[:4]})