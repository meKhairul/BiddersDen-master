from django.urls import re_path
from user import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^user/$', views.userView),
    re_path(r'^login/$', views.login),
    re_path(r'^logout/$', views.logout),
    re_path(r'^SaveFile/$', views.SaveFile)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 