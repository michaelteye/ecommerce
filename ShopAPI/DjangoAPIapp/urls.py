from django.urls import path
from .views import ListCategory,DetailCategory,ListBook,DetailBook,ListProduct,DetailProduct
urlpatterns = [
    path('categories', ListCategory.as_view(), name='category'),
    path('categorie/<int:pk>/', DetailCategory.as_view(), name='singlecategory'),
    path('books', ListBook.as_view(), name='books'),
    path('book/number/<int:pk>', DetailBook.as_view(),name='singlebook'),
    path('products',ListProduct.as_view(),name='products'),
    path('product<int:pk>/',DetailProduct.as_view(), name='singleproduct'),
]