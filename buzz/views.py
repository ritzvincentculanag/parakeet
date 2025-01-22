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
    form = BuzzCreateForm()

    if request.method == 'POST':
        form = BuzzCreateForm(data=request.POST)
        
        if form.is_valid:
            buzz = form.save(commit=False)
            buzz.author = request.user
            buzz.save()
            
            return redirect(to=reverse('buzz:buzz_list'))

    return render(
        request=request,
        template_name='buzz/create.html',
        context={ 'form': form }
    )