from rest_framework import serializers
from .models import Restaurant, Menu, Category, MenuItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    menu_items = MenuItemSerializer(many=True, source='menuitem_set')

    class Meta:
        model = Menu
        fields = ['categories','menu_items']

class RestaurantSerializer(serializers.ModelSerializer):
    menu = MenuSerializer()

    class Meta:
        model = Restaurant
        fields = '__all__'
