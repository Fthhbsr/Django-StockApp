from rest_framework import serializers
from .models import Brand, Firm, Product, TransactionStock, Category


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = "__all__"

class FirmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Firm
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()     # default read_only=True
    brand_id = serializers.IntegerField(write_only=True)
    category = serializers.StringRelatedField()     # default read_only=True
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Product
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    # product = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = "__all__"

class TransactionStockSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()     # default read_only=True
    product_id = serializers.IntegerField(write_only=True)
    user = serializers.StringRelatedField()     # default read_only=True
    user_id = serializers.IntegerField(write_only=True)
    firm = serializers.StringRelatedField()     # default read_only=True
    firm_id = serializers.IntegerField(write_only=True)

    

    class Meta:
        model = TransactionStock
        # fields = "__all__"
        exclude = ("price_total",)
        # read_only_fields = ("price_total",)       
    
    def create(self, validated_data):
        # print(validated_data)
        quantity = validated_data['quantity']
        price = validated_data['price']
        validated_data['price_total'] = quantity * price        
        transaction = TransactionStock.objects.create(**validated_data)    
        transaction.save()
        return transaction
    
    def validate(self, data):
        transaction = data['transaction']
        product_id = data['product_id']
        quantity = data['quantity']
        stock = Product.objects.filter(id=product_id).values()
        
        # print(product)

        if transaction == 'IN':
            new_stock = stock[0]['stock'] + quantity
            
        elif quantity <= stock[0]['stock'] :
            new_stock =  stock[0]['stock'] - quantity

        else:
            new_stock = stock[0]['stock']
            raise serializers.ValidationError(
                {"quantity": "product stock quantity is not enough..."}
            )        
        
        Product.objects.filter(id=product_id).update(stock=new_stock)

        print(new_stock)
        print(data)
        
        return data



