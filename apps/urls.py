from django.urls import path

from apps.views import AppList, AppTypesList, AppCreate, AppUpdate

urlpatterns = [
    path('app-types/', AppTypesList.as_view()),
    path('apps/', AppList.as_view()),
    path('apps/create', AppCreate.as_view()),
    path('apps/update', AppUpdate.as_view()),
]
