from django.shortcuts import render, get_object_or_404
from .models import Picture

def all_photos(request):
    photos = Picture.objects.order_by('-date')
    return render(request, 'gallery/all_photos.html', {'photos':photos})

def gallery(request,photo_id):
    photo = get_object_or_404(Picture, pk=photo_id)
    return render(request, 'gallery/gallery.html', {'photo':photo})