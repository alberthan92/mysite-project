"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings


from mysite import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),


    url(r'', include('blog.urls', namespace='blog')),
    url(r'^member/', include('member.urls', namespace='member')),
    url(r'^video/', include('video.urls', namespace='video')),
    url(r'^sns/', include('sns.urls', namespace='sns')),
    url(r'^photo', include('photo.urls', namespace='photo')),
    url(r'^error/$', views.error, name='error')
    # url(r'^test/(?P<pk1>[0-9]+)/(?P<pk2>[0-9]+)/$', test, name='test')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
