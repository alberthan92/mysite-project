from django.db import models
from django.utils import timezone
from datetime import datetime
# from django.utils.dateparse import parse_datetime
from django.contrib.auth.models import User
from django.conf import settings
from apis.mail import send_mail
from apis.sms import send_sms

class Post(models.Model):
    # author = models.ForeignKey('auth.User')
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=50)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(null=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey(Post)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)
        # print(self.post.author.email)
        # recipient_list = [self.post.author.email]
        title = 'A comment on the {} has been posted.'.format(self.post.title)
        content = '{} has been added on {}.'.format(
            self.content,
            self.created_date.strftime('%Y.%m.%d %H:%M')
        )
        number = self.post.author.phone_number
        # send_mail('A comment has been posted', 'Please check via Facebook')
        send_mail(title, content)

        send_sms(number, content)


