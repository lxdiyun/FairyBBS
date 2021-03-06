from django.conf.urls import include, url
from fairy import settings
from django.contrib import admin
from django.conf.urls.static import static
import forum

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'fairy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('forum.urls')),
    url(r'^user/', include('account.urls')),
    url(r'^api/forum/', include(forum.urls.api_urlpatterns)),
    url(r'^panel/', include('panel.urls', namespace='panel', app_name='panel')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
