from django.shortcuts import redirect, render, get_object_or_404
from .models import Product, ReviewRating
from category.models import Category
from carts.models import CartItem
from carts.views import _cart_id
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import ReviewForm
from django.contrib import messages
from orders.models import OrderProduct


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

    try:
        orderproduct = OrderProduct.objects.filter(
            user=request.user, product=product).exists()
    except OrderProduct.DoesNotExist:
        orderproduct = None

    # Get the reviews
    reviews = ReviewRating.objects.filter(product=product, status=True)

    context = {
        'product': product,
        'in_cart': in_cart,
        'color_variation': color_variation,
        'size_variation': size_variation,
        'orderproduct': orderproduct,
        'reviews': reviews,
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


def submit_review(request, product_id):
    url = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(
                user=request.user, product=product)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(
                request, 'Thank you! Your review has been updated')
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product = product
                data.user = request.user
                data.save()
                messages.success(
                    request, 'Thank you! Your review has been submitted')
                return redirect(url)
