from django.urls import path

from . import views

urlpatterns = [
    path(
        route='',
        view=views.buzz_list,
        name='buzz_list'
    ),
    path(
        route='create/',
        view=views.buzz_create,
        name='buzz_create'
    ),
    path(
        route='delete/<int:id>/',
        view=views.buzz_delete,
        name='buzz_delete'
    )
]
