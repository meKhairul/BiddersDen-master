from django.urls import re_path
from user import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^users/$', views.user),
    re_path(r'^users/(?P<pk>[0-9]+)$', views.user_detail),
    re_path(r'^profile/([a-zA-Z0-9_.-])$', views.login),
    re_path(r'^SaveFile/$', views.SaveFile)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)