from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from ..forms import PhotoForm
from ..models import Album, Photo, PhotoLike, PhotoDislike

__all__ = [
    'photo_add',
    'photo_like'
]

@login_required
def photo_add(request, album_pk):
    album = get_object_or_404(Album, pk=album_pk)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            img = form.cleaned_data['img']
            Photo.objects.create(
                album=album,
                owner=request.user,
                title=title,
                description=description,
                img=img,
            )
            return redirect('photo:album_detail', pk=album_pk)
    else:
        form = PhotoForm()
    context = {
        'form': form
    }
    return render(request, 'photo/photo_add.html', context)


@login_required
@require_POST
def photo_like(request, pk, like_type='like'):
    photo = get_object_or_404(Photo, pk=pk)
    album = photo.album
    next_path = request.GET.get('next')
    like_model = PhotoLike if like_type == 'like' else PhotoDislike
    opposite_model = PhotoDislike if like_type == 'like' else PhotoLike

    user_like_exist = like_model.objects.filter(
        user=request.user,
        photo=photo
    )

    if user_like_exist.exists():
        user_like_exist.delete()

    else:
        like_model.objects.create(
            user=request.user,
            photo=photo
        )
        opposite_model.objects.filter(
            user=request.user,
            photo=photo
        ).delete()

    if next_path:
        return redirect(next_path)
    else:
        return redirect('photo:album_detail', pk=album.pk)