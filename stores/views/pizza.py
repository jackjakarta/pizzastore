from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView

from stores.models import Pizza


class PizzaList(ListView):
    model = Pizza
    context_object_name = 'pizza_list'
    template_name = 'stores/pizza/list.html'
    paginate_by = 6


def pizza_list_view(request):
    pizza_list = Pizza.objects.all()
    paginator = Paginator(pizza_list, 9)

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    return render(request, "stores/pizza/list.html", {
        "page_obj": page_obj,
    })
