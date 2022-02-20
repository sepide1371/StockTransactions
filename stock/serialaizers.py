from rest_framework import serializers


class DynamicFieldsSerializer(serializers.Serializer):
    """
    A Serializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

class DynamicFieldsModelSerializer(serializers.ModelSerializer, DynamicFieldsSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """


class TradeInfoSerializer(DynamicFieldsSerializer):
    date = serializers.DateField(required=True)

class GetStockInfoOutputSerializer(DynamicFieldsSerializer):
    hEven = serializers.IntegerField()
    pTran = serializers.FloatField()
    qTitTran = serializers.IntegerField()


# class testSerializer(DynamicFieldsSerializer):
#     tradeHistory = serializers.ListField(child=GetStockInfoOutputSerializer(many=True))
