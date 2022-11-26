import datetime

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import DetailView, TemplateView, ListView

from Cart.models import Cart
from Products.models import Category, Products, Reviews


class ProductList(ListView):
    template_name = 'product-list.html'
    model = Products
    paginate_by = 20
    context_object_name = 'products'
    ordering = '-id'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get('cart_id', None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = None
        context['cart'] = cart
        return context


class CategoryDetail(View):
    def get(self, request, pk):
        category = Category.objects.get(pk=pk)
        product = Products.objects.filter(category=category)
        cart_id = self.request.session.get('cart_id', None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = None
        cart = cart
        return render(request, 'category_detail.html', {'category': category, 'product': product, 'cart': cart})


class ProductDetail(View):
    def get(self, request, pk):
        product = Products.objects.get(pk=pk)
        reviews = Reviews.objects.filter(product=product)
        related_products = Products.objects.filter(category=product.category).exclude(pk=pk)
        cart_id = self.request.session.get('cart_id', None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = None
        cart = cart
        context = {'product': product, 'reviews': reviews, 'related_products': related_products, 'cart': cart}
        return render(request, 'product-detail.html', context)

    def post(self, request, pk):
        product = Products.objects.get(pk=pk)
        user = request.user
        review = request.POST.get('review')
        name = request.POST.get('name')
        email = request.POST.get('email')
        rev = Reviews()
        rev.review = review
        rev.name = name
        rev.email = email
        rev.product = product
        rev.user = user
        rev.save()
        return redirect('ProductDetail', pk)


class SearchProducts(View):
    def get(self, request):
        search = request.GET.get('search')
        product = Products.objects.all().filter(name__icontains=search).order_by('name')
        cart_id = self.request.session.get('cart_id', None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = None
        cart = cart

        context = {'product': product, 'cart': cart}
        return render(request, 'search.html', context)


class FavouritesPage(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('LoginPage')
        else:
            product = Products.objects.filter(favourite=True, user=request.user)
            total_products_in_favourites = product.count()
            cart_id = self.request.session.get('cart_id', None)
            if cart_id:
                cart = Cart.objects.get(id=cart_id)
            else:
                cart = None
            cart = cart

            context = {'product': product,
                       'total_products_in_favourites': total_products_in_favourites,
                       'cart': cart
                       }
            return render(request, 'favourites.html', context)


class AddToFavourites(View):
    def get(self, request, pk):
        product = Products.objects.get(pk=pk)
        if not product.favourite:
            product.favourite = True
            product.user = request.user
            product.save()
            messages.info(request, 'product added to favourites successfully')
            return redirect('FavouritesPage')
        if product.favourite and product.user == request.user:
            messages.info(request, 'products already in your favourites')
            return redirect('FavouritesPage')
        if product.favourite and not product.user == request.user:
            product.favourite = True
            product.user = request.user
            product.save()
            return redirect('FavouritesPage')


class RemoveFavourite(View):
    def get(self, request, pk):
        product = Products.objects.get(pk=pk)
        if product.favourite:
            product.favourite = False
            product.save()
            messages.info(request, 'product removed in favourites')
            return redirect("FavouritesPage")
