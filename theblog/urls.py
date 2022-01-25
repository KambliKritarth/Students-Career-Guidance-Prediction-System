from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView, submitmyform,ScoreView, ContactView, AddQueryView


urlpatterns = [
    #path('',views.home, name="home"),
    path('',HomeView.as_view(),name = "home"),
    path('article/<int:pk>',ArticleDetailView.as_view(),name = 'article-detail'),
    path('form/',views.myform,name = 'fill_form'),
    path('submitmyform',views.submitmyform,name = 'submitmyform'),
    path('careeroptions',views.careeroptions,name ='careeroptions'),
    path('aptitude',views.aptitude,name = 'aptitude'),
    path('aptitude_cse',views.aptitude_cse,name = 'aptitude_cse'),
    path('aptitude_extc',views.aptitude_extc,name = 'aptitude_extc'),
    path('contact',views.contact,name = 'contact'),
    path('article/<int:pk>/query/',AddQueryView.as_view(),name='add_query'),
    #path('query_success',views.contact,name='query_added'),
]
