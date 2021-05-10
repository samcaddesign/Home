
from django.contrib import admin
from django.urls import path
from website.views import about_view, services_view, serives_id, contact_view, softwares_view, softwares_id, header_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aboutus', about_view, name="aboutus"),
    path('services', services_view, name="services"),
    path('services/<str:id>', serives_id, name="services_id"),
    path('contact', contact_view, name="contact"),
    path('softwares', softwares_view, name="softwares"),
    path('softwares/<str:id>', softwares_id, name="softwares_id"),
    path('base', header_view, name="base")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
