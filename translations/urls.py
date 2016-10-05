from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()



js_info_dict = {
    'domain': 'djangojs',
    'packages': ('myapp',),
}



urlpatterns = patterns('',
    # Examples:
    url(r'^home/$', 'myapp.views.home', name='home'),
    url(r'^contact/$', 'myapp.views.contact', name='contact'),
    url(r'^about/$', 'myapp.views.about_us', name='about_us'),
    url(r'^support/$', 'myapp.views.support', name='support'),

    #url(r'^myapp/', include('translations.myapp.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^jsi18n/$', 'django.views.i18n.javascript_catalog', js_info_dict),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )
