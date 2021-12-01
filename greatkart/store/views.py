from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from carts.models import CartItem
from carts.views import _cart_id
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def store(request, category_slug=None):
    if category_slug != None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True)
        paginator = Paginator(products, 1)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        products_count = products.count()
    else:
        products = Product.objects.filter(is_available=True).order_by('id')
        paginator = Paginator(products, 5)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        products_count = products.count()

    context = {
        'products': paged_products,
        'products_count': products_count,
    }
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        product = Product.objects.get(
            category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(
            cart__cart_id=_cart_id(request), product=product).exists()
        color_variation = product.variation_set.colors()
        size_variation = product.variation_set.sizes()
    except Exception as e:
        raise e
    context = {
        'product': product,
        'in_cart': in_cart,
        'color_variation': color_variation,
        'size_variation': size_variation
    }
    return render(request, 'store/product_detail.html', context)


def search(request):
    keyword = request.GET.get('keyword') if request.GET.get(
        'keyword') != None else ''
    products = Product.objects.order_by(
        '-created_date').filter(
            Q(category__slug__icontains=keyword) | Q(product_name__icontains=keyword) | Q(description__icontains=keyword))
    products_count = products.count()
    context = {
        'products': products,
        'products_count': products_count
    }
    return render(request, 'store/store.html', context)
