from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login,name="login"),
    path('signup/',views.signup),
    path('userlist/',views.userlist),
    path('posts/',views.post_feed),
    path('profile/<str:userid>/',views.profile,name="Profile"),
    path('addpost/',views.postForm,name="MakePost"),
    path('viewpost/<str:id>/',views.viewPost,name="ViewPost"),
    path('editpost/<str:id>/',views.editPostForm,name="EditPost"),
    path('deletepost/<str:id>/',views.deletePostForm,name="DeletePost"),
    path('logout/',views.logoutPage),
]