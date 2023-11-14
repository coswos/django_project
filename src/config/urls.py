from django.contrib import admin
from django.urls import path

from issues import api as issue_api
from users import api as user_api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/all/", user_api.all_users),
    path("users/create/", user_api.create_user),
    path("issues/create/", issue_api.create_issue),
    path("issues/all/", issue_api.all_issues),
]
