from django.urls import path
from .import views as v


urlpatterns = [
    path('addalbum', v.add_album),
    path('albumlist', v.album_list),
    path('delete_album/<int:id>', v.delete_album),
    path('update_album/<int:id>', v.update_album),
    path('album_api', v.CreateListAlbum.as_view()),
    path('detailalbum_api/<int:pk>', v.UpdateDeleteGetAlbum.as_view()),
    path('album_library', v.album_library)

    # path('listcreatealbum', v.ListCreateAlbum.as_view()),
    # path('getupdatedeletealbum/<pk>', v.GetUpdateDestroyAlbum.as_view())

]
