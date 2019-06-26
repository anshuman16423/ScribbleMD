from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'newnote', views.new_note),
    url(r'preview', views.preview),
    url(r'logout', views.logout),
    url(r'view/(?P<note_id>(\d+))', views.view, name='note_id'),
    url(r'edit/(?P<note_id>(\d+))', views.edit, name='note_id'),
    url(r'delete/(?P<note_id>(\d+))', views.delete, name='note_id'),
    url(r'download/(?P<note_id>(\d+))', views.download, name='note_id'),
]
