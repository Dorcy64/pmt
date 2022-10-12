from rest_framework import viewsets
from tweets.models import Tweet
from tweets.serializers import TweetSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


@api_view(['GET', 'POST'])
def tweet_list(request):
    if request.method == 'GET':
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
