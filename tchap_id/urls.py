"""tchap_id URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
#from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from matrix_connect.views import profile, MatrixLoginView
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^profile/', profile),
    url(r'^login/', MatrixLoginView.as_view(), name='login'),
#    url(r'^logout/', LogoutView.as_view(), name='logout')
]
