from django.shortcuts import render
from .models import Braille

# Create your views here.
def home(request):
    return render(request,'home.html')


def braille_image_upload(request):
    braille_image = Braille()
    braille_image.images = request.FILES['images']
    braille_image.save()

    return render(request,'home.html')

def calculation(request):
    b_image = Braille.objects.last()

    return render(request,'calculation.html',{'b_image':b_image})

def calculation(request):
    b_image = Braille.objects.last()
    #여기서 이제 b_image를 가지고 계산

    return render(request,'calculation.html',{'b_image':b_image})
    