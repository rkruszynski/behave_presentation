from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import History, User


def login(request):
    return render(request, 'app/login.html')


@login_required
def base(request):
    return render(request, 'app/main.html')


@login_required
def unauthorized(request):
    return render(request, 'app/unauthorized.html')


@login_required
def foo(request):
    return render(request, 'app/foo.html')


@login_required
def user_profile(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'app/user_profile.html', {
        "user_profile": user
    })


@staff_member_required(login_url='unauthorized')
def clear_logs(request):
    # Remove all items from the history data-table
    History.objects.all().delete()
    return redirect('history')


@staff_member_required(login_url='unauthorized')
def new_user(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user = User.objects.create_user(**user_form.cleaned_data)
            user.save()

            messages.success(request, 'BADUM TSS')
            return HttpResponseRedirect('new_user')

    else:
        user_form = UserForm()

    return render(request, 'app/new_user.html', {
        'user_form': user_form,
    })


@staff_member_required(login_url='unauthorized')
def history_view(request):

    # Get the data
    query = request.GET.get('q')
    if query:
        history = History.objects.filter(user__username=query).order_by('-login_details')
    else:
        history = History.objects.order_by('-login_details').all()

    # Pagination setup
    paginator = Paginator(history, 5)
    page = request.GET.get('page')

    try:
        history_items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        history_items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        history_items = paginator.page(paginator.num_pages)

    return render(
        request, 'app/history.html', {'history': history_items}
    )
