
from django.contrib import admin
from django.urls import path
from article import views
import userprofile.views
import comment.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.article_list),
    # path('article/',views.article_list),
    path('list/',views.article_list,name='list'),
    path('user/',views.user_list),
    path('detail/<int:id>',views.article_detail,name='detail'),
    path('create/',views.article_create,name='create'),
    path('delete/<int:id>',views.article_delete,name='delete'),
    path('update/<int:id>',views.article_update,name='update'),
    path('login/',userprofile.views.user_login,name='login'),
    path('logout/',userprofile.views.user_logout,name='logout'),
    path('register/', userprofile.views.user_register, name='register' ),
    path('comment/<int:id>/', comment.views.post_comment, name='post_comment' ),
]
