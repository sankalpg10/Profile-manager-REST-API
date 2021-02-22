from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
# we do not need to provide basename in UserProfileViewSet case because we have provided the query set to the viewset and django will figure it out based on the query set.
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path("hello-view/", views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
# router.urls is a list that is saved in the router object when we register urls with it
