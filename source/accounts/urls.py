from django.urls import path

from accounts.views import LoginView, RegisterView, ProfileView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    # path('profile/<int:pk>/change', UserChangeView.as_view(), name='change')
]
