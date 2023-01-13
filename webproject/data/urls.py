from . import views
from django.urls import path


urlpatterns = [
    path('',views.data,name='data'),
    path('add',views.add,name='create'),
    path('<int:pk>',views.DataDetailView.as_view(), name='news-detail') #<int:pk> pk necessarily
]
