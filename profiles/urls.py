from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="Home"),
    # path('profile',views.profile,name="profile" ),
]