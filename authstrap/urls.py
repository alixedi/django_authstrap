from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',

        url(r'^auth/login/$',
            auth_views.login,
            {'template_name': 'auth/login.html'},
            name='auth_login'),

        url(r'^auth/logout/$',
            auth_views.logout,
            {'template_name': 'auth/logout.html'},
            name='auth_logout'),

        url(r'^auth/password/change/$',
            auth_views.password_change,
            {'template_name': 'auth/password_change_form.html'},
            name='auth_password_change'),

        url(r'^auth/password/change/done/$',
            auth_views.password_change_done,
            {'template_name': 'auth/password_change_done.html'},
            name='auth_password_change_done'),

        url(r'^auth/password/reset/$',
            auth_views.password_reset,
            {'template_name': 'auth/password_reset_form.html'},
             name='auth_password_reset'),

        url(r'^auth/password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
            auth_views.password_reset_confirm,
            {'template_name': 'auth/password_reset_confirm.html'},
            name='auth_password_reset_confirm'),

        url(r'^auth/password/reset/complete/$',
            auth_views.password_reset_complete,
            {'template_name': 'auth/password_reset_complete.html'},
            name='auth_password_reset_complete'),

        url(r'^auth/password/reset/done/$',
            auth_views.password_reset_done,
            {'template_name': 'auth/password_change_done.html'},
            name='auth_password_reset_done'),
    )