from django.urls import path
from .import views as v

urlpatterns = [
    path('add_artist', v.add_artist),
    path('artist_list', v.artist_list),
    path('delete_artist', v.delete_artist),
    path('update_artist/<int:id>', v.update_artist),
    path('artist_api', v.CreateListArtist.as_view()),
    path('detailartist_api/<int:pk>', v.UpdateDeleteGetArtist.as_view()),
    path('artist_library', v.artist_library),
    # path('listcreateartist', v.ListCreateArtist.as_view()),
    # path('getupdatedeleteartist/<pk>', v.GetUpdateDestroyArtist.as_view())
]
