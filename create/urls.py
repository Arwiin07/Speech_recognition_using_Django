from django.urls import path
from . import views

urlpatterns = [
    path('', views.login,name="login"),
    path('lists',views.lists,name="lists"),
    path('choosing_between',views.choosing,name="choose"),
    path('chosen_file/',views.second_page,name="chosen_file"),
    path('transcript/',views.index,name="index"),
    # path('next',views.audio_process,name="index"),
    path('audiofile/process/', views.audio_process,name = 'audioprocess'),
    path('<id>', views.detail_view,name="detail_view" ),
]