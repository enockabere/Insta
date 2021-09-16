from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index,name="index"),
    path('home/',views.home,name="home" ),
    path('personal/',views.account,name="personal" ),
    path('like/',views.LikeView,name="like_post" ),
    path("register", views.register_request, name="register")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)