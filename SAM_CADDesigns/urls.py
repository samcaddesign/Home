
from django.contrib import admin
from django.urls import path
from website.views import need_view, services_view, serives_id, contact_view, softwares_view, header_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('need', need_view),
    path('services', services_view, name="services"),
    path('services/<str:id>', serives_id, name="services_id"),
    path('contact', contact_view),
    path('softwares', softwares_view, name="softwares"),
    path('base', header_view, name="base")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
