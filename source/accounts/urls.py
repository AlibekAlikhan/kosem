from django.urls import path

from accounts.views import RegisterUserView, LoginUserView, LogoutUserView

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('logout/', LogoutUserView.as_view(), name='auth_logout'),
    # # path('profile/<int:pk>/change', UserChangeView.as_view(), name='change')
]
