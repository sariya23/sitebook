from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from sitebook import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("books.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Админка"
admin.site.index_title = "Книгиии"
