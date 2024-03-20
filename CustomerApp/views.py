from django.shortcuts import render
from DjangoEcommerceApp.models import Products
from django.core.paginator import Paginator
from django.db.models import Count

def customer_view(request):
    search_query = request.GET.get('search')

    # Get unique subcategories from products
    subcategories = Products.objects.values('subcategories_id__title').annotate(total=Count('subcategories_id')).order_by('subcategories_id')

    if search_query:
        products = Products.objects.filter(product_name__icontains=search_query)
    else:
        products = Products.objects.all()

    products = products.order_by('-created_at')

    paginator = Paginator(products, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'customer_view.html', {'page_obj': page_obj, 'subcategories': subcategories})