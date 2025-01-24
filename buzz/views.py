from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib import messages

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
        
        if form.is_valid():
            buzz = form.save(commit=False)
            buzz.author = request.user
            buzz.save()

            messages.success(
                request=request,
                message='Buzz created successfully!'
            )
            
            return redirect(to=reverse('buzz:buzz_list'))

    return render(
        request=request,
        template_name='buzz/create.html',
        context={ 'form': form }
    )

def buzz_delete(request, id):
    buzz = get_object_or_404(klass=Buzz, id=id)

    if request.method == 'POST':
        buzz.delete()

        messages.success(
            request=request,
            message='Buzz deleted successfully!'
        )

        return redirect(reverse('buzz:buzz_list'))

    return render(
        request=request,
        template_name='buzz/delete.html',
        context={ 'buzz': buzz }
    )

