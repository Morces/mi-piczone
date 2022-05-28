from django.shortcuts import render

from gallery.models import Image, Location



# Create your views here.
def index(request):
    images = Image.get_all_images()
    locations = Location.objects.all()
    title = 'piczone'

    return render(request, 'gallery/index.html')