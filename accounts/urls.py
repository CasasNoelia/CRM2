from django.urls import path
from .import views

urlpatterns = [

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),


    path('', views.home, name="home"),
    path('empleo/', views.empleo, name="empleo"),    #products

    path('usuario/<str:pk_test>/',views.usuario,name="usuario"), #custumer

    path('create_recibo/',views.createRecibo, name="create_recibo"),   #'create_order/',views.createOrder, name="create_order"
    path('update_recibo/<str:pk>/',views.updateRecibo, name="update_recibo"),
    path('informacion/', views.Informacion, name="informacion"),
    path('delete_recibo/<str:pk>/',views.deleteRecibo, name="delete_recibo")
]

