import json

from django.shortcuts import get_object_or_404, redirect
from ..models import Photo, PhotoLike, PhotoDislike
from django.http import HttpResponse

__all__ = [
    'photo_like',
]

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
        msg = 'delete'

    else:
        like_model.objects.create(
            user=request.user,
            photo=photo
        )
        opposite_model.objects.filter(
            user=request.user,
            photo=photo
        ).delete()
        msg = 'created'


    ret = {
        'msg': msg
    }
    return redirect(json.dumps(ret), content_type='application/json')