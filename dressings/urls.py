from django.conf.urls import patterns, include, url
from django.conf import settings
from . import views 

urlpatterns = patterns('',
    url(
        regex=r'^$',
        view=views.DressingFilterView.as_view(),
        name="dressing_filter",
    ),
    url(
        regex=r'^dressings/$',
        view=views.DressingListView.as_view(),
        name="dressing_list",
    ),
    url(
        regex=r'^wounds/$',
        view=views.WoundListView.as_view(),
        name="wound_list",  
    ),
    url(
        regex=r'^wounds/new/$',
        view=views.WoundCreateView.as_view(),
        name="wound_create",  
    ),
    url(
        regex=r'^dressings/(?P<slug>[\w-]+)/$',
        view=views.DressingDetailView.as_view(),
        name="dressing_detail",
    ),
)


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (
            r'^static/(?P<path>.*)$',
             'django.views.static.serve',
            {
                'document_root': settings.STATIC_ROOT
            }
        ),
        (
            r'^media/(?P<path>.*)$',
             'django.views.static.serve',
            {
                'document_root': settings.MEDIA_ROOT
            }
        ),
    )