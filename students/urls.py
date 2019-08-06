from django.conf.urls import url
from . import views
app_name = "students"

urlpatterns = [
    #students/
    url(r'^$', views.insert_view, name="inset_view"),

    #students/display
    url(r'^display$', views.display, name='display'),

    #students/delete
    url(r'^delete$', views.delete, name='delete'),

    #students/search
    url(r'^search$', views.search, name='search'),
]