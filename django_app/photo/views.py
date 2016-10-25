from django.shortcuts import render
from photo.models import Album

def album_list(request):
    albums = Album.objects.all()
    return render(request, 'photo/album_list.html', {'album_list': albums})