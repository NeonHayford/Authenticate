from django.contrib import admin
from django.urls import path, include
from Authentication import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Authentication.urls')),
    path('', views.index, name='home'),
    path('passwordChange/done/', views.passwordChangeDone, name='password_change_done'),
    path('resetPage/<uidb64>/<token>/', views.resetPageView, name='reset_page'),
    path('resetPage/done/', views.resetPageDone, name='reset_page_done'),
]
