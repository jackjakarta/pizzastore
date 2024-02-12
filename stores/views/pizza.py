from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from django.views.generic import ListView
from stores.models import Pizza


def pizza_list_view(request):
    pizza_list = Pizza.objects.all().order_by('price')
    paginator = Paginator(pizza_list, 9)

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    print(page_obj)

    return render(request, 'stores/pizza/list.html', {
        'page_obj': page_obj,
    })