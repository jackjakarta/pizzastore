from django.views.generic import ListView

from stores.models import Store


class StoreList(ListView):
    model = Store
    context_object_name = 'store_list'
    template_name = 'stores/store/list.html'
    paginate_by = 6
