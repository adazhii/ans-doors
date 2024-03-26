from rest_framework import serializers

from origindb.models import Inventre, Invendet, Inventry, Incompdet


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventre
        fields = ('recno5', 'autoid', 'tree_descr',)


class ComponentSerializer(serializers.ModelSerializer):
    descr_1 = serializers.CharField(source='origin_product.descr_1')

    class Meta:
        model = Invendet
        fields = ('recno5', 'autoid', 'category', 'comp_id', 'descr_1')


class ComponentDetailSerializer(serializers.ModelSerializer):
    descr_1 = serializers.CharField(source='origin_product.descr_1')

    class Meta:
        model = Incompdet
        fields = ('recno5', 'autoid', 'category', 'comp_id', 'descr_1')


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='origin_category.tree_descr')
    components = ComponentSerializer(source='origin_components_detail_as_product', many=True)

    class Meta:
        model = Inventry
        fields = (
            'recno5', 'autoid', 'id', 'descr_1', 'category', 'components'
        )
