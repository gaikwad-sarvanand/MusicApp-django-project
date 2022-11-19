from django.urls import path, include
from . import views as v


urlpatterns = [
    path('add_song', v.add_song),
    path('song_list', v.song_list),
    path('delete_song/<int:id>', v.delete_song),
    path('update_song/<int:id>', v.update_song),
    path('song_api', v.CreateListSong.as_view()),
    path('detailsong_api/<int:pk>', v.UpdateDeleteGetSong.as_view()),
    path('song_library', v.song_library)

    # path('listcreatesong', v.CreateListSong.as_view()),
    # path('getupdatedeletesong/<pk>', v.GetUpdateDestroySong.as_view()),

]
