from django.urls import path
from .views import Products

urlpatterns=[
    path('',Products.as_view()),
    # path('',views.index),
    # path('create',views.create),
    # path('delete',views.delete)

]