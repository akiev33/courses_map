from rest_framework import serializers

from .models import Favorite


class FavoriteCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

    def create(self, validated_data):
        news1 = validated_data.get('news')
        user1 = self.context.get('user')
        favorite = Favorite.objects.create(news=news1, user=user1)

        return favorite