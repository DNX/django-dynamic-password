from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'testapp.views.login_view', name='login'),
)
