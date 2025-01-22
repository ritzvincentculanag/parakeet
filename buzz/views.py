from django.shortcuts import redirect, render
from django.urls import reverse

from buzz.models import Buzz
from buzz.forms import BuzzCreateForm


def buzz_list(request):
    buzzes = Buzz.published.all()

    return render(
        request=request,
        template_name='buzz/list.html',
        context={ 'buzzes': buzzes }
    )

def buzz_create(request):
    form = None

    if request.method != 'POST':
        form = BuzzCreateForm()
    else:
        form = BuzzCreateForm(data=request.GET)
        form.save(commit=False)
        form.author = request.user
        form.save()

        return redirect(to=reverse('buzz:buzz_list'))

    return render(
        request=request,
        template_name='buzz/create.html',
        context={ 'form': form }
    )