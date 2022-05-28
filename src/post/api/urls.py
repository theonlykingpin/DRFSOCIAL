from django.urls import path, re_path
from post.api.views import PostListCreateView, PostRetrieveUpdateDestroyView


app_name = 'post'

urlpatterns = [
    path('', PostListCreateView.as_view(), name='post-list-create'),
    path('<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='post-retrieve-update-destroy'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', PostRetrieveUpdateDestroyView.as_view(), name='post-retrieve-update-destroy'),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', PostRetrieveUpdateDestroyView.as_view(), name='post-retrieve-update-destroy'),
]
