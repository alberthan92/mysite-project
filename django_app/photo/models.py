from django.db import models
from django.conf import settings

class Album(models.Model):
    title = models.CharField(max_length=30)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    description = models.CharField(max_length=800, blank=True)


class Photo(models.Model):
    album = models.ForeignKey(Album)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=80, blank=True)
    img = models.ImageField(upload_to='photo')
    img_thumbnail = models.ImageField(upload_to='photo/thumbnail', blank=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, through='PhotoLike', related_name='photo_set_like_users')
    dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL, through='PhotoDislike', related_name='photo_set_dislike_users')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        image_changed = False

        if self.pk:
            ori = Photo.objects.get(pk=self.pk)
            if ori.img != self.img:
                image_changed = True

        if self.img and not self.img_thumbnail:
            image_changed = True

        super().save(*args, **kwargs)
        if image_changed:
            self.make_thumbnail()

    def url_thumbnail(self):
        return self.url_field('img_thumbnail')

    def make_thumbnail(self):
        import os
        from PIL import Image, ImageOps
        from io import BytesIO
        from django.core.files.base import ContentFile
        from django.core.files.storage import default_storage

        size = (300, 300)
        f = default_storage.open(self.img)
        image = Image.open(f)
        ftype = image.format

        image = ImageOps.fit(image, size, Image.ANTIALIAS)

        path, ext = os.path.splitext(self.img.name)
        name = os.path.basename(path)

        thumbnail_name = '%s_thumb%s' % (name, ext)

        temp_file = BytesIO()
        image.save(temp_file, ftype)
        temp_file.seek(0)

        content_file = ContentFile(temp_file.read())
        self.img_thumbnail.save(thumbnail_name, content_file)

        temp_file.close()
        content_file.close()
        f.close()
        return True


class PhotoLike(models.Model):
    photo = models.ForeignKey(Photo)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_date = models.DateTimeField(auto_now_add=True)


class PhotoDislike(models.Model):
    photo = models.ForeignKey(Photo)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_date = models.DateTimeField(auto_now_add=True)