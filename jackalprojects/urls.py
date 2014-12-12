from jackalprojects import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

__author__ = 'cemkiy'
__author__ = 'barisariburnu'
__author__ = 'kaykisizcom'

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jackalprojects.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^$', 'jackalprojects.views.home_page', name='home'),
    url(r'^member/', include('member.urls')),
    url(r'^bitcoin/', include('bitcoin.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/'}),
    url(r'^ticket_pool/$', 'jackalprojects.views.ticket_pool'),
    url(r'^public_profile/(.+)$', 'jackalprojects.views.public_profile'),
    url(r'^contact_us/$', 'jackalprojects.views.contact_us'),
    url(r'^forgotten_password/$', 'jackalprojects.views.forgotten_password'),
    url(r'^sorry/$', 'jackalprojects.views.page_sorry'),
) + staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
#    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#        'document_root': settings.MEDIA_ROOT})
