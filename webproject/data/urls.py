from . import views
from django.urls import path


urlpatterns = [
    path('',views.data,name='data'),
    path('add',views.add,name='create'),
    path('<int:pk>',views.DataDetailView.as_view(), name='news-detail'), #<int:pk> pk necessarily
    path('<int:pk>/update',views.DataUpdatelView.as_view(), name='news-update'),
    path('<int:pk>/delete',views.DataDeletelView.as_view(), name='news-delete'),
]
