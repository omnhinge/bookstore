from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    
    # Cart URLs
    path('cart/', views.view_cart, name='view_cart'),
    path('add-to-cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    
    # Book Management URLs
    path('manage-books/', views.manage_books, name='manage_books'),
    path('add-book/', views.add_book, name='add_book'),
    path('update-cart-item/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('edit_book/<int:id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:id>/', views.delete_book, name='delete_book'),
]



# from django.urls import path
# from . import views
# from django.conf.urls import url
# from django.urls import re_path


# urlpatterns = [
#     path('', views.home, name='home'),
#     path('', views.home, name='home'),
#     path('register/', views.register, name='register'),
#     path('login/', views.user_login, name='login'),
#     path('logout/', views.user_logout, name='logout'),
    
#     # Cart URLs
#     path('cart/', views.view_cart, name='view_cart'),
#     path('add-to-cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
#     path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    
#     # Book Management URLs
#     path('manage-books/', views.manage_books, name='manage_books'),
#     path('add-book/', views.add_book, name='add_book'),
#     path('update-cart-item/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
#     path('edit_book/<int:id>/', views.edit_book, name='edit_book'),
#     path('delete_book/<int:id>/', views.delete_book, name='delete_book'),
# ]



# from django.urls import path
# from . import views
# from django.conf.urls import url
# from django.urls import re_path


# urlpatterns = [
#     path('', views.home, name='home'),
#     path('', views.home, name='home'),
#     path('register/', views.register, name='register'),
#     path('login/', views.user_login, name='login'),
#     path('logout/', views.user_logout, name='logout'),
    
#     # Cart URLs
#     path('cart/', views.view_cart, name='view_cart'),
#     path('add-to-cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
#     path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    
#     # Book Management URLs
#     path('manage-books/', views.manage_books, name='manage_books'),
#     path('add-book/', views.add_book, name='add_book'),
#     path('update-cart-item/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
#     path('edit_book/<int:id>/', views.edit_book, name='edit_book'),
#     path('delete_book/<int:id>/', views.delete_book, name='delete_book'),
# ]