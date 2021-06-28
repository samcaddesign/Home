
from django.contrib import admin
from django.urls import path
from website.views import * 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aboutus', about_view, name="aboutus"),
    path('services', services_view, name="services"),
    path('services/<str:serviceName>', serivces_id, name="services_id"),
    path('contact', contact_view, name="contact"),
    path('softwares', softwares_view, name="softwares"),
    path('softwares/<str:softwareName>', softwares_id, name="softwares_id"),
    path('', home_view, name="home"),
    path('base', base_view, name="base"),
    path('home', home_view, name="home"),
    path('login',login_view, name="login"),
    path('register',profile_view, name="register"),
    path('profile',p_view, name="profile"),
    path('logout',logout_view,name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
