from django.urls import path
from .views import SignupView, LoginView, MeView, LogoutView
from .views import (
    AdminUserListView,
    ActivateUserView,
    DeactivateUserView,
    UpdateProfileView,
    ChangePasswordView,
)



urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('login/', LoginView.as_view()),
    path('me/', MeView.as_view()),
    path('admin/users/', AdminUserListView.as_view()),
    path('admin/users/<int:user_id>/activate/', ActivateUserView.as_view()),
    path('admin/users/<int:user_id>/deactivate/', DeactivateUserView.as_view()),
    path('profile/', UpdateProfileView.as_view()),
    path('change-password/', ChangePasswordView.as_view()),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('admin/users/', AdminUserListView.as_view()),

]
