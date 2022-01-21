from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("movies", include("movies.urls", namespace="movies")),
    path("books", include("books.urls", namespace="books")),
    path("genres", include("categories.urls", namespace="genres")),
    path("people", include("people.urls", namespace="people")),
    path("admin/", admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)