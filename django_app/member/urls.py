from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^login/facebook/$', views.login_facebook, name='login_facebook'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signup2/$', views.signup2, name='signup2'),
    url(r'^signup3/$', views.signup3, name='signup3'),
    url(r'^login/facebook/$', views.login_facebook, name='login_facebook')
]