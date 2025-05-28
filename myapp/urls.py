from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.signin,name='root'),
    path('signin/',views.signin,name='signin'),
    path('home/',views.home,name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(next_page='signin'), name='logout'),
    path('chattoai/', views.chattoai, name='chattoai'),
    path('chattopdf/', views.chattopdf, name='chattopdf'),
    path('builownai/', views.builtownai, name='builtownai'),
    # path('upload/', views.upload_pdf, name='upload_pdf'),
    path('setting/', views.setting, name='setting'),
]
