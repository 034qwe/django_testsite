from . import views
from django.urls import path


urlpatterns = [
    path('',views.DataPage.as_view(),name='data'),
    path('add',views.AddPage.as_view(),name='create'),
    path('post/<slug:post_slug>',views.ShowPost.as_view(), name='news-detail'), 
    path('<int:pk>/update',views.DataUpdatelView.as_view(), name='news-update'),
    path('<int:pk>/delete',views.DataDeletelView.as_view(), name='news-delete'),
    path('login/',views.login,name='login'),
    path('category/<slug:cat_slug>/',views.show_category, name='category'),

]
