from django.urls import path

from my_music_app_stan_v2.web.views import album_add, album_details, album_edit, album_delete, home_page, \
    profile_create, profile_details, profile_delete

urlpatterns = [
    path('album/add/', album_add, name='album add'),
    path('album/details/<int:pk>/', album_details, name='album details'),
    path('album/edit/<int:pk>/', album_edit, name='album edit'),
    path('album/delete/<int:pk>/ ', album_delete, name='album delete'),

    path('', home_page, name='home with profile'),
    path('profile/create/', profile_create, name='home with no profile'),
    path('profile/details/ ', profile_details, name='profile details'),
    path('profile/delete/', profile_delete, name='profile delete'),
]
