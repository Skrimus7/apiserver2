from rest_framework import serializers

from .models import Items


class ItemsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    uuid = serializers.UUIDField()
    parent_uuid = serializers.UUIDField()
    type = serializers.CharField(max_length=20)
    name = serializers.CharField()
    meta = serializers.CharField()
    data = serializers.CharField()
    modified = serializers.DateTimeField()

    def create(self, validated_data):
        return Items.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.uuid = validated_data.get('uuid', instance.uuid)
        instance.parent_uuid = validated_data.get('parent_uuid', instance.parent_uuid)
        instance.type = validated_data.get('type', instance.type)
        instance.name = validated_data.get('name', instance.name)
        instance.meta = validated_data.get('meta', instance.meta)
        instance.data = validated_data.get('data', instance.data)
        instance.modified = validated_data.get('modified', instance.modified)
        instance.save()
        return instance
