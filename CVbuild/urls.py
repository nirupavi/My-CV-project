"""CVbuild URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from CVapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.signup_page,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/', views.logout_page,name='logout'),
    path('changepass/',views.change_pass,name='changepass'),
    path('cvmaker/',views.Homeview.as_view(),name='cvmaker'),
    path('<int:pk>',views.resumeview.as_view(),name='resumeview'),
    path('delete/<int:id>/',views.delete_data,name='deletedata'),
    path('<int:id>/',views.update_data,name='updatedata'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
