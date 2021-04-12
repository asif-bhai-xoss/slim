from django.db import models
from user_control.models import *


class BookModel(models.Model):
    publisher = models.ForeignKey(PublisherProfileModel, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)
    edition = models.CharField(max_length=255)
    buy_price = models.DecimalField(max_digits=7, decimal_places=2)
    sell_price = models.DecimalField(max_digits=7, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)


# class OrderModel(models.Model):
#     student = models.ForeignKey(StudentProfileModel, on_delete=models.SET_NULL, null=True, blank=True)
#     date_ordered = models.DateTimeField(auto_now_add=True)
#     completed = models.BooleanField(default=False)
#     transaction_id = models.CharField(max_length=200, null=True)
#
#
# class OrderItemModel(models.Model):
#     book = models.ForeignKey(BookModel, on_delete=models.CASCADE)
#     order = models.ForeignKey(OrderModel, on_delete=models.SET_NULL, null=True, blank=True)
#     quantity = models.IntegerField(default=0, null=True, blank=True)
#     date_added = models.DateTimeField(auto_now_add=True)
