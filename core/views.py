from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView

from Cart.models import Cart
from Products.models import Category, Products
from core.forms import CustomerCommentForm
from core.models import Contact, CustomerComments


class Homepage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['product'] = Products.objects.all()
        context['customercomments'] = CustomerComments.objects.all()
        cart_id = self.request.session.get('cart_id', None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = None
        context['cart'] = cart
        return context


class ContactUs(View):

    def get(self, request):
        cart_id = self.request.session.get('cart_id', None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = None
        cart = cart
        return render(request, 'contact.html', {'cart': cart})

    def post(self, request):
        contact = Contact()
        contact.save_feedback(request=request)
        return render(request, 'contact.html')


class AddCustomerComment(View):
    def get(self, request):
        form = CustomerCommentForm(request.POST)
        cart_id = self.request.session.get('cart_id', None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = None
        cart = cart
        return render(request, 'customer_comment.html', {'form': form, 'cart': cart})

    def post(self, request):
        form = CustomerCommentForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return render(request, 'customer_comment.html', {'form': form})
