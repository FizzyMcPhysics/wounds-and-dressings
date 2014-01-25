from django.conf.urls import patterns, include, url

from . import views 

urlpatterns = patterns('',
    url(
        regex=r'^$',
        view=views.WoundListView.as_view(),
        name="wound_list",
    ),
    url(
        regex=r'^dressings/$',
        view=views.DressingListView.as_view(),
        name="dressing_list",  
    ),
    url(
        regex=r'^dressings/(?P<slug>[\w]+)/$',
        view=views.DressingDetailView.as_view(),
        name="dressing_detail",
    ),
)
