from django.urls import path
from . import views

urlpatterns = [
    path('', views.office_transactions_grid, name='office-transactions'),
    path('add/', views.add_transaction, name='add-transaction'),

    # path('add-transaction', views.add_transaction, name='add-transaction'),
]