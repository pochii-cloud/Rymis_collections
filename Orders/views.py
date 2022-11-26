# import requests
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import TemplateView, DeleteView, UpdateView

from Cart.models import Cart, CartProduct
from Orders.models import Order
from Region.models import Town
from core.forms import OrderCodeForm


class MyOrders(LoginRequiredMixin, View):
    login_url = '/Accounts/LoginPage/'

    def get(self, request):
        orders = Order.objects.all().filter(user=request.user)
        cart_id = self.request.session.get('cart_id', None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = None

        return render(request, 'Myorders.html', {'orders': orders, 'cart': cart})

    # def post(self, request):
    #     order = Order.objects.get(id=request.POST['order_id'])
    #     res = requests.post('http://localhost:8000/mpesa/online/lipa/',
    #                         data={'PhoneNumber': order.mobile, 'Amount': order.total})
    #     return redirect('BaseView')


class CancelOrder(DeleteView):
    model = Order
    success_url = '/'
    template_name = 'delete.html'


#
# class UpdateOrder(UpdateView):
#     template_name = 'update_cake_details.html'
#     model = Order
#     fields = ['ordered_by', 'ordered_by', 'mobile', 'total', 'order_status', ]
#     success_url = '/ManageCakes/'


class AddOrderCodes(View):
    def get(self, request, pk):
        form = OrderCodeForm()
        order = Order.objects.get(pk=pk)
        context = {'form': form, 'order': order}
        return render(request, 'Add_Order_Codes.html', context)

    def post(self, request, pk):
        form = OrderCodeForm(request.POST)
        order = Order.objects.get(pk=pk)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.order = order
            form.save()
            messages.info(request, 'Code submitted Thankyou..Wait For Confirmation')
        context = {'form': form, 'order': order}
        return render(request, 'Add_Order_Codes.html', context)


class OrderDetails(View):
    def get(self, request, pk):
        order = Order.objects.get(pk=pk)
        cartproducts = CartProduct.objects.filter(cart=order.cart)
        context = {'cartproducts': cartproducts, 'order': order}
        return render(request, 'order_details.html', context)
