from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += [
    url(r'^catalog/', include('catalog.urls')),
]

urlpatterns += [
    # url(r'^$', RedirectView.as_view(url='/catalog/', permanent=False)),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)