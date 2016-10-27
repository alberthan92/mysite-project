from django.shortcuts import render
from ..models import Album

__all__ = [
    'album_list',
]

def album_list(request):
    albums = Album.objects.all()
    context = {
        'album_list': albums,
    }
    return render(request, 'photo/album_list.html', context)