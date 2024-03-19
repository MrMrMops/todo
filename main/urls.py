from django.urls import path
from .views import *

urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('addtodo/',TodoAddPageView.as_view(),name='addtodo'),
    path('page/<int:pk>/',TodoPageView.as_view(),name='post'),
    path('register/',RegisterUserView.as_view(),name='register'),
    path('login/',LoginUserView.as_view(),name='login'),
    path('logout/',LogoutUserView,name='logout'),
    path('delete/<int:pk>', TodoDeleteView.as_view(), name='delete'),
    path('self',SelfView.as_view(),name='self'),

    path('profile/<int:pk>/', ShowProfileView.as_view(), name='profile'),
    # path('register/', CreateProfileView.as_view(),name='createprofile'),
    path('update/<int:pk>/',UpdateProfileView.as_view(),name='update'),
]
