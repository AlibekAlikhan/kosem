from django.urls import path

from webapp.views.gallery import GalleryView, GalleryCreateView, GalleryDeleteView, GalleryUpdateView, GalleryDetailView

from accounts.views import logout_view

from api.views import favorites_api

urlpatterns = [
    path('', GalleryView.as_view(), name='index'),
    path('gallery/create', GalleryCreateView.as_view(), name='gallery_create'),
    path('logout/', logout_view, name='logout'),
    path('article/<int:pk>', GalleryDetailView.as_view(), name="detail_view"),
    path('article/<int:pk>/update', GalleryUpdateView.as_view(), name="gallery_update"),
    path('article/<int:pk>/delit', GalleryDeleteView.as_view(), name="gallery_delit"),
    path('article/<int:pk>/delit/confirm', GalleryDeleteView.as_view(), name="confirm"),
]