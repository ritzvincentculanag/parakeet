from django.urls import path

from . import views

urlpatterns = [
    path(
        route='',
        view=views.buzz_list,
        name='buzz_list'
    )
]
