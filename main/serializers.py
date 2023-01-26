from rest_framework import serializers
from .models import Tag, Event


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('__all__')


class EventsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        exclude = ('description',)


class EventSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    tags = TagSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.event_type = validated_data.get('event_type', instance.event_type)
        instance.description = validated_data.get('description', instance.description)
        instance.category = validated_data.get('category', instance.category)
        instance.tags.set(validated_data.get('tags', instance.tags.all()))
        instance.save()

        return instance

    class Meta:
        model = Event
        fields = ('__all__')
        extra_kwargs = {'event_type': {'required': False},
                        'description': {'required': False},
                        'category': {'required': False}}
