from django.urls import path
from .views import PostList, PostDetail

app_name = 'app_api'

# One view to show a list of all posts (the homepage), one view to show an individual post
urlpatterns = [ 
    path('<int:pk>/', PostDetail.as_view(), name='detailcreate'), # individual
    path('', PostList.as_view(), name='listcreate') # list
]
 