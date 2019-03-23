from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.company_views import CompanyList
from .views.user_views import UserList, Logout
from .views.post_views import PostView
from .views.comment_views import CommentDetail, CommentView

router = DefaultRouter()
router.register(r'posts', PostView)
router.register(r'comments', CommentView)
router.register('users', UserList)


urlpatterns = [
    path('', include(router.urls)),
    path('posts/<str:pk>/comments/', CommentDetail.as_view()),
    path('companies/', CompanyList.as_view()),
    path('logout', Logout.as_view()),
    #path('users/', UserList.as_view()),


]
