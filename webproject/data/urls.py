from . import views
from django.urls import path


urlpatterns = [
    path('',views.data,name='data'),
    path('add',views.add,name='create'),
    path('post/<slug:post_slug>',views.show_post, name='news-detail'), 
    path('<int:pk>/update',views.DataUpdatelView.as_view(), name='news-update'),
    path('<int:pk>/delete',views.DataDeletelView.as_view(), name='news-delete'),
    path('login/',views.login,name='login'),
    path('category/<slug:url_id>/',views.show_category, name='category'),
    path('create',views.add_page,name='add'),
]
