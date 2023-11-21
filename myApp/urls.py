from django.urls import path

from myApp import views


urlpatterns = [
    path('',views.signupPage,name="signup"),
    path('login',views.loginPage,name="login"),
    path('home',views.homePage,name="home"),
    path('logout',views.logoutPage,name="logout"),
    path('add',views.addpage,name="add"),
    path('edit/<str:id>',views.editPage,name="edit"),
    path('delete/<str:id>',views.deleteStudent,name="delete"),
]
