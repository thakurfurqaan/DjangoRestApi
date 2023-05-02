from django.urls import path
from .views import PostList
from .views import MyTokenObtainPairView

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
