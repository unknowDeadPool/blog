from django.urls import path
from applications.post.views import *

urlpatterns = [
    # path('', PostListAPIView.as_view()),
    # path('create/', PostCreateAPIView.as_view()),

    # path('update/<int:pk>/', PostUpdateAPIView.as_view()),
    # path('delete/<int:pk>/', PostDeleteAPIView.as_view()),
    # path('detail/<int:pk>/', PostDetailAPIView.as_view()),
    path('<int:pk>/', PostDetailDeleteUpdateAPIView.as_view())
]