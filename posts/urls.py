from django.urls import path
from . import views

urlpatterns = [
    path('posts',views.index,name='index'),
    path('posts/details/<int:id>',views.details,name='details')
]