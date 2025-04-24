from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Book, Cart, CartItem, UserProfile

# Authentication Views
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                UserProfile.objects.create(user=user)
                login(request, user)
                messages.success(request, 'Registration successful!')
                return redirect('home')
        else:
            messages.error(request, 'Passwords do not match')
    
    return render(request, 'bookstore/register.html')

from django.contrib.auth import authenticate, login

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'bookstore/login.html')

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')

# Book Views
def home(request):
    books = Book.objects.all()
    return render(request, 'bookstore/home.html', {'books': books})

@login_required
def manage_books(request):
    if not request.user.userprofile.is_root_user:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('home')
    
    books = Book.objects.all()
    return render(request, 'bookstore/manage_books.html', {'books': books})

@login_required
def add_book(request):
    if not request.user.userprofile.is_root_user:
        return redirect('home')
        
    if request.method == 'POST':
        try:
            book = Book.objects.create(
                title=request.POST.get('title'),
                author=request.POST.get('author'),
                description=request.POST.get('description'),
                price=float(request.POST.get('price')),
                stock=int(request.POST.get('stock'))
            )
            if 'cover_image' in request.FILES:
                book.cover_image = request.FILES['cover_image']
                book.save()
            messages.success(request, 'Book added successfully!')
            return redirect('manage_books')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
    
    return render(request, 'bookstore/add_book.html')

# Cart Views
@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()
    return render(request, 'bookstore/cart.html', {
        'cart': cart,
        'cart_items': cart_items
    })

@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    messages.success(request, f'{book.title} added to your cart!')
    return redirect('view_cart')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    messages.success(request, 'Item removed from your cart.')
    return redirect('view_cart')
@login_required
def update_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, 'Cart updated!')
        else:
            cart_item.delete()
            messages.success(request, 'Item removed from cart')
    return redirect('view_cart')

from .decorators import root_user_required

@root_user_required
def manage_books(request):
    books = Book.objects.all()
    return render(request, 'bookstore/manage_books.html', {'books': books})



from django.db import transaction
from django.template.loader import get_template, TemplateDoesNotExist
from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404, redirect
from .models import Book

def edit_book(request, id):
    book = get_object_or_404(Book, pk=id)

    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.price = request.POST['price']
        book.stock = request.POST['stock']
        book.description
        book.save()
        return redirect('manage_books')  # or wherever your list is

    return render(request, 'bookstore/edit_book.html', {'book': book})

def delete_book(request, id):
    book = get_object_or_404(Book, pk=id)

    if request.method == 'POST':
        with transaction.atomic():
            book.delete()
        return redirect('manage_books')  # or 'book_list' or whatever your list page is

    return render(request, 'bookstore/delete_book.html', {'book': book})