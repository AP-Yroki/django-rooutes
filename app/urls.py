from django.urls import path, include
from .views import index
from . import views

product_patterns = [
    path("", views.posts),
    path('new', views.new),
    path('top', views.top),
    path("likes", views.likes),
    path("comments", views.comments),
]


urlpatterns = [
    path('', index, name='index'),
    path('user/', views.user),
    path('posts/<str:id>/', include(product_patterns), name='posts'),
    path('about/', views.about),
    path('contacts/', views.contacts),
    path('details/', views.details),
    path('access', views.access, name='access'), # http://127.0.0.1:8000/access?username=admin&password=admin
    path("set/", views.set),
    path("get/", views.get),
    path('redirect_about/', views.redirect_about),
    path('redirect_contacts/', views.redirect_contacts),
    path('pernament_redirect_about/', views.pernament_redirect_about),
    path('pernament_redirect_contacts/', views.pernament_redirect_contacts),
    path('page_not_found/', views.page_not_found),
    path('json/', views.json),
]