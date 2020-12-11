from rest_framework import serializers


class ItemsSerializer(serializers.Serializer):
    category = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=100)
    desc = serializers.CharField()
    price = serializers.DecimalField(max_digits=7,decimal_places=2)
    seller = serializers.CharField(max_length=100)
    image = serializers.ImageField()
    rating = serializers.IntegerField()



class cartSerializer(serializers.Serializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    date_ordered = serializers.DateTimeField()
    complete = serializers.BooleanField()
    transaction_id = serializers.CharField()
    total_bill = serializers.DecimalField(max_digits=7,decimal_places=2)
    total_quantity = serializers.IntegerField()

class cartItemSerializer(serializers.Serializer):
    item = serializers.SlugRelatedField(read_only=True,slug_field='name')
    order = serializers.StringRelatedField()
    quantity = serializers.IntegerField()
    date_added = serializers.DateTimeField()