from django.core.paginator import Paginator
from django.shortcuts import render, redirect, Http404, get_object_or_404, reverse

from stores.models import Pizza
from stores.utils.cart import Cart


def pizza_list_view(request):
    pizza_list = Pizza.objects.all().order_by('price')
    paginator = Paginator(pizza_list, 9)

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    print(page_obj)

    return render(request, 'stores/pizza/list.html', {
        'page_obj': page_obj,
    })


def add_to_cart(request, pizza_id):
    # pizza = get_object_or_404(Pizza, pk=pizza_id)
    page_number = request.POST.get('page', 1)

    try:
        quantity = int(request.POST.get('quantity'))
    except ValueError as e:
        raise Http404(e)

    cart = Cart(request.user, request.session)
    cart.update(pizza_id, quantity)

    return redirect(f"{reverse('stores:pizza:list')}?page={page_number}")
