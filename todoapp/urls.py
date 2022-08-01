
from django.urls import path
# from todoapp.views import index,login,signup
from todoapp import views

urlpatterns = [
    path("", views.index, name='home'),
    path('login', views.login,name='login'),
    path("signup",views.signup ,name='signup'),
    path("addtodo",views.addtodo),
    path("logout",views.signout),
    path("delete-todo/<int:id>",views.delete_todo),
    path('change_status/<int:id>/<str:status>',views.change_status)
]
