from django.urls import path
from .views import *
from django.views.i18n import set_language

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('publications/', Publications.as_view(), name='publications'),
    path('article/<int:pk>/', ArticleDetail.as_view(), name='article_detail'),
    path('favourites/', Favourites.as_view(), name='favourites'),
    path('publish/', Publish.as_view(), name='publish'),
    path('add_fav/', AddFav.as_view(), name='add_fav'),
    path('set_language/', set_language, name='set_language'),
]
