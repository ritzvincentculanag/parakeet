from django.shortcuts import render

from buzz.models import Buzz


def buzz_list(request):
    buzzes = Buzz.published.all()

    return render(
        request=request,
        template_name='buzz/list.html',
        context={ 'buzzes': buzzes }
    )
