from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from .models import Book, Cart, CartItem, UserProfile
from .forms import UserRegisterForm, UserLoginForm, BookForm

def home(request):
    books = Book.objects.all()  # This line is crucial
    return render(request, 'bookstore/home.html', {'books': books})

from django.contrib.auth.views import LoginView
class UserLoginView(LoginView):
    template_name = 'bookstore/login.html'
    form_class = UserLoginForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create user profile
            UserProfile.objects.create(user=user)
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'bookstore/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'bookstore/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()
    return render(request, 'bookstore/cart.html', {'cart': cart, 'cart_items': cart_items})

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
            messages.success(request, 'Item removed from your cart.')
    return redirect('view_cart')

# Root user views
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
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('home')
    
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added successfully!')
            return redirect('manage_books')
    else:
        form = BookForm()
    return render(request, 'bookstore/add_book.html', {'form': form})

@login_required
def edit_book(request, book_id):
    if not request.user.userprofile.is_root_user:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('home')
    
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('manage_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookstore/edit_book.html', {'form': form, 'book': book})

@login_required
def delete_book(request, book_id):
    if not request.user.userprofile.is_root_user:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('home')
    
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('manage_books')
    return render(request, 'bookstore/delete_book.html', {'book': book})