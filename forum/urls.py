from django.conf.urls import url, include
from django.contrib import admin
from forum.views import get_page
from forum.views import get_name_and_date
from forum.views import get_post_titles
from forum.views import get_post_id
from forum.views import get_author_by_id


urlpatterns = [
    url(r'^page/(?P<page>[\d-]+)', get_page),
    url(r'^home/(?P<name>[\w-]+)', get_name_and_date),
    url(r'^all/$',get_post_titles),
    url(r'^get/(?P<id>[\d-]+)', get_post_id),
    url(r'^get_author/(?P<id>[\d-]+)', get_author_by_id),

]