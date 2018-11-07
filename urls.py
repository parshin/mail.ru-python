from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^simple_route/$', views.simple_route, name='simple_route'),
    url(r'^slug_route/(?P<slug>[a-z]-\d[a-z]\_[a-z]\d)/$', views.slug_route, name='slug_route'),
    url(r'^sum_route/(?P<digit1>-?\d)/(?P<digit2>-?\d)/$', views.sum_route, name='sum_route'),
    url(r'^sum_get_method/$', views.sum_get_method, name='sum_get_method'),
    url(r'^sum_post_method/$', views.sum_post_method, name='sum_post_method'),

]