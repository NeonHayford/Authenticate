"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Authentication import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Authentication.urls')),
    path('', views.index, name='home'),
    # path('passwordChange/done/', views.passwordChangeDone.as_view(template_name='templates/reset_pages_template/password_change_done.html'), name='password_change_done'),
    path('resetPage/<uidb64>/<token>/', views.resetPageView.as_view(template_name='templates/reset_pages_template/reset_page.html'), name='reset_page'),
    path('resetPage/done/', views.resetPageDoneView.as_view(template_name='templates/reset_pages_template/reset_page_done.html'), name='reset_page_done'),
]
