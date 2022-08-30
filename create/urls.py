from django.urls import path
from . import views

urlpatterns = [
    path('', views.login,name="login"),
    path('transcript/',views.index,name="index"),
    # path('next',views.audio_process,name="index"),
    path('audiofile/process/', views.audio_process,name = 'audioprocess')
]