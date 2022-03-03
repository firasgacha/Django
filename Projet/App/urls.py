from django.urls import path, include
from . import views
from .views import Affiche

urlpatterns = [
    path('a/', views.index),
    path('index/<int:classe>', views.index_param),
    path('index_template/', views.index_template),
    path('affiche/', views.Affiche),
    path('affiche1/', Affiche.as_view(),name='liste'),
    path('ajouter/',views.ajouter,name='ajouter'),
    path('ajouter2/',views.ajouterP.as_view()),
    path('delete/<int:id>',views.delete,name='supp'),
    path('delete2/<int:pk>',views.deleteP.as_view(),name='supp2'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register,name='register'),
    path('home/',views.home,name='home')
]
