from django.urls import path

from webapp.views import NewAcsesView

urlpatterns = [
    path('category/asd', NewAcsesView.as_view(), name="categoryasd_list"),
]
