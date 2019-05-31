from django.urls import path

from . import views
app_name = "leader"
urlpatterns = [
    path('',views.Index.as_view(), name="index"),
    path('addmem',views.addMember.as_view(), name="addmem"),
]