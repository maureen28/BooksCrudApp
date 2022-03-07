from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post_book', views.book_creation, name='post_book'),
    path('view_book/<int:book_id>', views.book_detail, name='view_book'),
    path('update_book/<int:book_id>', views.update_book, name='update_book'),
    path('delete_book/<int:book_id>', views.delete_book, name='delete_book'),
]