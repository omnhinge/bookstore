from django.contrib import admin
from .models import Book, UserProfile, Cart, CartItem

admin.site.register(Book)
admin.site.register(UserProfile)
admin.site.register(Cart)
admin.site.register(CartItem)