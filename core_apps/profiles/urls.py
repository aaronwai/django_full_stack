from django.urls import path
from .views import (
    AvatarUploadAPIView,
    ProfileDetailAPIView,
    ProfileListAPIView,
    ProfileUpdateAPIView,
    NonTenantProfileListAPIView
)


urlpatterns = [
    path("all/", ProfileListAPIView.as_view(), name="profile-list"),
    path("non-tenant-profiles/", NonTenantProfileListAPIView.as_view(), name="non-tenant-profiles"),
    path("user/my-profile/", ProfileDetailAPIView.as_view(), name="profile-details"),
    path("user/update/", ProfileUpdateAPIView.as_view(), name="profile-update"),
     path("user/avatar/", AvatarUploadAPIView.as_view(), name="avatar-upload"),
]
