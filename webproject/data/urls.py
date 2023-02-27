from . import views
from django.urls import path
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('',cache_page(60)(views.DataPage.as_view()),name='data'),
    path('add',views.AddPage.as_view(),name='create'),
    path('post/<slug:post_slug>',views.ShowPost.as_view(), name='news-detail'), 
    path('<int:pk>/update',views.DataUpdatelView.as_view(), name='news-update'),
    path('<int:pk>/delete',views.DataDeletelView.as_view(), name='news-delete'),
    path('register/',views.RegisterUser.as_view(),name='register'),
    path('login/',views.LoginUser.as_view(),name='login'),
    path('category/<slug:cat_slug>/',views.show_category, name='category'),
    path('logout/',views.logout_user,name='logout'),
    path('contact/',views.ContactView.as_view(),name='contact')

]
