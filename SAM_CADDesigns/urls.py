
from django.contrib import admin
from django.urls import path
from website.views import need_view, services_view, ser_det, contact_view, softwares_view, base_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('need', need_view),
    path('service', services_view, name="services"),
    path('service/<str:id>', ser_det, name="services"),
    path('contact', contact_view),
    path('softwares', softwares_view),
    path('base', base_view)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
