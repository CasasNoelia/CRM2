from django.urls import path
from django.urls import path
from .import views

urlpatterns = [

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),


    path('', views.home, name="home"),

    path('create_empleo/', views.createEmpleo, name="create_empleo"),
    path('update_empleo/<str:pk>/',views.updateEmpleo, name="update_empleo"),
    path('delete_empleo/<str:pk>/',views.deleteEmpleo, name="delete_empleo"),

    path('usuario/<str:pk_test>/',views.usuario,name="usuario"),

    path('create_recibo/',views.createRecibo, name="create_recibo"),
    path('update_recibo/<str:pk>/',views.updateRecibo, name="update_recibo"),
    path('delete_recibo/<str:pk>/',views.deleteRecibo, name="delete_recibo"),
    path('informacion/', views.Informacion, name="informacion")

]

