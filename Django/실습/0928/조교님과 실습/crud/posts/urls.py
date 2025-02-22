from django.urls import path
from . import views

# url namespace
# url을 이름으로 분류하는 기능

app_name = "posts"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("delete/<int:todo_pk>", views.delete, name="delete"),
]
