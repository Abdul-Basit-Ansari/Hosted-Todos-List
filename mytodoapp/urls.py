from django.urls import path
from . import views

urlpatterns = [
    path('',views.index ,name="index" ),
    path('addtodo',views.addtodo ,name="addtodo" ),

    path('signup',views.signup , name="signup"),
    path('login',views.ulogin , name="login"),
    path('logout/',views.ulogout ,name="logout" ),
    path('delete/<int:sno>',views.udelete ,name="delete" ),
]
