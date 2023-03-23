from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('frontend.urls')),
    path('', include('courses.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path(
        "ckeditor5/",
        include('django_ckeditor_5.urls'),
        name="ck_editor_5_upload_file"
    ),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
