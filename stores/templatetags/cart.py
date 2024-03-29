from django import template
from stores.models import Pizza

register = template.Library()


@register.filter(name='products_or_price')
def get_products_number_or_price(cart_dict, type_=None):
    print('!! cart dict is', cart_dict)
    if type_ == 'price':
        pizza_list = Pizza.objects.filter(id__in=cart_dict.keys())
        return '%.2f' % sum([pizza.price * cart_dict[str(pizza.id)] for pizza in pizza_list])

    return sum([int(cart_value) for cart_value in cart_dict.values()])


@register.simple_tag(name='cart_data', takes_context=True)
def get_cart_data(context):
    cart_dict = context.request.session.get('cart', {})
    pizza_list = Pizza.objects.filter(id__in=cart_dict.keys())
    products_number = sum([int(cart_value) for cart_value in cart_dict.values()])
    total_price = '%.2f RON' % sum([pizza.price * cart_dict[str(pizza.id)] for pizza in pizza_list])

    return {
        'products': products_number,
        'price': total_price
    }


@register.filter(name='visible_pages')
def visible_pages(page_obj):
    paginator = page_obj.paginator
    pages = list(paginator)
    current_page = page_obj.number
    first_pages = pages[0:2]
    last_pages = pages[-2:]

    if current_page == 1 or current_page == paginator.num_pages:
        return first_pages + [None] + last_pages

    current_page_index = [page.number for page in pages].index(current_page)
    return first_pages + [None] + pages[current_page_index-1:current_page_index+2] + [None] + last_pages


@register.filter(name='pizza_value')
def get_pizza_value_from_cart(session, pizza_id):
    return session['cart'].get(str(pizza_id), 0) if 'cart' in session else 0
