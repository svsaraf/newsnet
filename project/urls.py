from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^$', 'app.views.index'),
    (r'^register$', 'app.views.register'),
    (r'^login/?$', 'app.views.login'),
    (r'^logout/?$', 'app.views.logout'),
    (r'^write/?$', 'app.views.publish'),
    (r'^publish/?$', 'app.views.publish'),
    (r'^user/(\d+)/$', 'app.views.userview'),
    (r'^accounts/login/', 'app.views.login'),
    (r'^list/(\d+)/$', 'app.views.list'),

    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^project/', include('project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
