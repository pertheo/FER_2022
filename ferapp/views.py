from django.shortcuts import render, loader
from .forms import UploadFileForm
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse
from .forms import ImageForm
from .ml_model.image_mode import dan_image

def index(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

@ensure_csrf_cookie
def upload_screen(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            print(file.name)
            handle_uploaded_file(file)
            return render(request, "upload_screen.html", {'filename': file.name})
    else:
        form = UploadFileForm()
    return render(request, 'upload_screen.html', {'form': form})

def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            
def upload_video(request):
  template = loader.get_template('upload_screen.html')
  return HttpResponse(template.render({}, request))

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            new_url = img_obj.image.url[1:]
            dan_image.main(new_url)
            fp=open('ferapp\ml_model\image_mode\emotion.txt','r')
            emotion=str(fp.readline())
            print(emotion)
            fp.close()
            return render(request, 'upload_image.html', {'form': form, 'img_obj': img_obj, 'emotion': emotion})
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})

    