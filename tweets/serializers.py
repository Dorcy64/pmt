from rest_framework import serializers
from tweets.models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    created_date = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = ('name', 'text', 'created_date', 'is_active')

    @staticmethod
    def get_created_date(obj):
        return obj.created_date.strftime("%m/%d/%Y, %H:%M:%S")
