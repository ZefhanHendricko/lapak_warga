from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Product, Order, Cart

def home(request):
    products = Product.objects.filter(is_active=True).select_related("seller", "category")[:8]
    return render(request, "marketplace/home.html", {"products": products})

def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        Cart.objects.get_or_create(user=user)
        messages.success(request, "Akun berhasil dibuat. Selamat datang di Lapak Warga!")
        return redirect("dashboard")
    return render(request, "registration/register.html", {"form": form})

@login_required
def dashboard(request):


    if request.user.is_superuser:

        context = {
            "total_users": User.objects.count(),
            "total_products": Product.objects.count(),
            "total_orders": Order.objects.count(),
            "recent_products": Product.objects.select_related(
                "seller", "category"
            )[:5],
        }

        return render(
            request,
            "marketplace/dashboard_admin.html",
            context
        )

    
    orders = Order.objects.filter(user=request.user)[:5]
    my_products = Product.objects.filter(seller=request.user)

    context = {
        "orders": orders,
        "product_count": my_products.count(),
        "order_count": Order.objects.filter(
            user=request.user
        ).count(),
        "recent_products": my_products[:4],
    }

    return render(
        request,
        "marketplace/dashboard.html",
        context
    )


def product_list(request):
    products = Product.objects.filter(is_active=True).select_related("seller", "category")
    return render(request, "marketplace/product_list.html", {"products": products})

def product_detail(request, slug):
    product = get_object_or_404(
        Product.objects.select_related("seller", "category"),
        slug=slug,
        is_active=True
    )

    return render(
        request,
        "marketplace/product_detail.html",
        {"product": product}
    )
    