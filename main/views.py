import datetime
import json
from django.http import (
    HttpResponse,
    HttpResponseRedirect,
    JsonResponse,
    HttpResponseNotAllowed
)
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.html import strip_tags
from django.views.decorators.http import require_POST
from main.forms import ProductForm
from main.models import Product


# ======================== SHOW MAIN ========================
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'npm': '2406496183',
        'name': request.user.username,
        'class': 'PBP F',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
    }
    return render(request, "main.html", context)


# ======================== CREATE PRODUCT ========================
@login_required(login_url='/login')
def create_Product(request):
    form = ProductForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)


# ======================== PRODUCT DETAIL ========================
@login_required(login_url='/login')
def show_Product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {'product': product}
    return render(request, "product_detail.html", context)


# ======================== JSON/XML ========================
def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")


def show_json(request):
    product_list = Product.objects.all()
    data = []
    for product in product_list:
        data.append({
            'id': str(product.id),
            'name': product.name,
            'price': str(product.price),
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'stock': product.stock,
            'size': product.size,
            'is_featured': product.is_featured,
            'is_signed': product.is_signed,
            'is_official_merch': product.is_official_merch,
            'user_id': product.user_id,
        })
    return JsonResponse(data, safe=False)


def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)


def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related("user").get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': str(product.price),
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'stock': product.stock,
            'size': product.size,
            'is_featured': product.is_featured,
            'is_signed': product.is_signed,
            'is_official_merch': product.is_official_merch,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)


# ======================== AUTH ========================
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    return render(request, 'register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm(request)
    return render(request, 'login.html', {'form': form})


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response


# ======================== EDIT PRODUCT ========================
@login_required(login_url='/login')
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)
    form = ProductForm(request.POST or None, instance=product)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Product updated successfully!")
        return redirect('main:show_main')

    return render(request, "edit_product.html", {'form': form, 'product': product})


# ======================== DELETE PRODUCT ========================
@login_required(login_url='/login')
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)
    product.delete()
    messages.success(request, "Product deleted successfully!")
    return HttpResponseRedirect(reverse('main:show_main'))


# ======================== ADD PRODUCT AJAX ========================
@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    try:
        name = strip_tags(request.POST.get("name", ""))
        price = int(request.POST.get("price") or 0)
        description = strip_tags(request.POST.get("description", ""))
        category = request.POST.get("category", "jersey")
        thumbnail = request.POST.get("thumbnail", "")
        stock = int(request.POST.get("stock") or 0)
        size = request.POST.get("size", "M")
        is_featured = request.POST.get("is_featured") == 'on'
        is_signed = request.POST.get("is_signed") == 'on'
        is_official_merch = request.POST.get("is_official_merch") == 'on'
        user = request.user if request.user.is_authenticated else None

        new_product = Product.objects.create(
            name=name,
            price=price,
            description=description,
            category=category,
            thumbnail=thumbnail,
            stock=stock,
            size=size,
            is_featured=is_featured,
            is_signed=is_signed,
            is_official_merch=is_official_merch,
            user=user,
        )

        return JsonResponse({
            "id": str(new_product.id),
            "name": new_product.name,
            "price": new_product.price,
            "description": new_product.description,
            "category": new_product.category,
            "thumbnail": new_product.thumbnail,
            "stock": new_product.stock,
            "size": new_product.size,
            "is_featured": new_product.is_featured,
            "is_signed": new_product.is_signed,
            "is_official_merch": new_product.is_official_merch,
            "user_id": new_product.user.id if new_product.user else None,
        }, status=201)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


# ======================== EDIT PRODUCT AJAX ========================
@login_required(login_url='/login')
@csrf_exempt
def edit_product_ajax(request, id):
    if request.method != "POST":
        return JsonResponse({'success': False, 'error': 'Method not allowed'}, status=405)

    try:
        product = get_object_or_404(Product, pk=id, user=request.user)

        product.name = request.POST.get('name', product.name)
        product.price = request.POST.get('price', product.price)
        product.description = request.POST.get('description', product.description)
        product.category = request.POST.get('category', product.category)
        product.thumbnail = request.POST.get('thumbnail', product.thumbnail)
        product.stock = request.POST.get('stock', product.stock)
        product.size = request.POST.get('size', product.size)
        product.is_featured = request.POST.get('is_featured') == 'on'
        product.is_signed = request.POST.get('is_signed') == 'on'
        product.is_official_merch = request.POST.get('is_official_merch') == 'on'
        product.save()

        return JsonResponse({
            'success': True,
            'message': 'Product updated successfully',
            'product': {
                'id': str(product.id),
                'name': product.name,
                'price': product.price,
                'description': product.description,
                'category': product.category,
                'thumbnail': product.thumbnail,
                'stock': product.stock,
                'size': product.size,
                'user_id': str(product.user.id),
            }
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)


# ======================== DELETE PRODUCT AJAX ========================
@login_required(login_url='/login')
@csrf_exempt
def delete_product_ajax(request, id):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    try:
        product = get_object_or_404(Product, id=id, user=request.user)
        product.delete()
        return JsonResponse({"success": True, "message": "Product deleted successfully"})
    except Product.DoesNotExist:
        return JsonResponse({"success": False, "message": "Product not found"}, status=404)
