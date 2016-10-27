from django.shortcuts import render, redirect
from ..models import Album
from ..forms import AlbumForm

__all__ = [
    'album_list',
    'album_add',
]

def album_list(request):
    albums = Album.objects.all()
    context = {
        'album_list': albums,
    }
    return render(request, 'photo/album_list.html', context)

def album_add(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            Album.objects.create(
                title=title,
                description=description,
                owner=request.user,
            )
            return redirect('photo:album_list')
        else:
            form = AlbumForm()
        context = {
            'form': form,
        }
        return render(request, 'photo/album_add.html', context)